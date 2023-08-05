import time
import math
import mock
import pytest

from async_jaeger.sampler import (
    ConstSampler,
    ProbabilisticSampler,
    RateLimitingSampler,
    GuaranteedThroughputProbabilisticSampler,
    AdaptiveSampler,
    get_sampling_probability,
    get_rate_limit,
)


MAX_INT = 1 << 63


def get_tags(type, param):
    return {
        'sampler.type': type,
        'sampler.param': param,
    }


def test_probabilistic_sampler_errors():
    with pytest.raises(AssertionError):
        ProbabilisticSampler(-0.1)
    with pytest.raises(AssertionError):
        ProbabilisticSampler(1.1)


def test_probabilistic_sampler():
    sampler = ProbabilisticSampler(0.5)
    assert MAX_INT == 0x8000000000000000
    sampled, tags = sampler.is_sampled(MAX_INT - 10)
    assert sampled
    assert tags == get_tags('probabilistic', 0.5)
    sampled, _ = sampler.is_sampled(MAX_INT + 10)
    assert not sampled
    sampler.close()
    assert '%s' % sampler == 'ProbabilisticSampler(0.5)'


def test_const_sampler():
    sampler = ConstSampler(True)
    sampled, _ = sampler.is_sampled(1)
    assert sampled
    sampled, _ = sampler.is_sampled(MAX_INT)
    assert sampled
    sampler = ConstSampler(False)
    sampled, tags = sampler.is_sampled(1)
    assert not sampled
    sampled, tags = sampler.is_sampled(MAX_INT)
    assert not sampled
    assert tags == get_tags('const', False)
    assert '%s' % sampler == 'ConstSampler(False)'


def test_rate_limiting_sampler():
    sampler = RateLimitingSampler(2)
    sampler.rate_limiter.balance = 2.0
    # stop time by overwriting timestamp() function to always return
    # the same time
    ts = time.time()
    sampler.rate_limiter.last_tick = ts
    with mock.patch('async_jaeger.rate_limiter.RateLimiter.timestamp') \
            as mock_time:
        mock_time.side_effect = lambda: ts  # always return same time
        assert sampler.rate_limiter.timestamp() == ts
        sampled, _ = sampler.is_sampled(0)
        assert sampled, 'initial balance allows first item'
        sampled, _ = sampler.is_sampled(0)
        assert sampled, 'initial balance allows second item'
        sampled, _ = sampler.is_sampled(0)
        assert not sampled, 'initial balance exhausted'

        # move time 250ms forward, not enough credits to pay for one sample
        mock_time.side_effect = lambda: ts + 0.25
        sampled, _ = sampler.is_sampled(0)
        assert not sampled, 'not enough time passed for full item'

        # move time 500ms forward, now enough credits to pay for one sample
        mock_time.side_effect = lambda: ts + 0.5
        sampled, _ = sampler.is_sampled(0)
        assert sampled, 'enough time for new item'
        sampled, _ = sampler.is_sampled(0)
        assert not sampled, 'no more balance'

        # move time 5s forward, enough to accumulate credits for 10 samples,
        # but it should still be capped at 2
        sampler.last_tick = ts  # reset the timer
        mock_time.side_effect = lambda: ts + 5
        sampled, _ = sampler.is_sampled(0)
        assert sampled, 'enough time for new item'
        sampled, _ = sampler.is_sampled(0)
        assert sampled, 'enough time for second new item'
        for i in range(0, 8):
            sampled, tags = sampler.is_sampled(0)
            assert not sampled, 'but no further, since time is stopped'
        assert tags == get_tags('ratelimiting', 2)
    sampler.close()
    assert '%s' % sampler == 'RateLimitingSampler(2)'

    # Test with rate limit of greater than 1 second
    sampler = RateLimitingSampler(0.1)
    sampler.rate_limiter.balance = 1.0
    ts = time.time()
    sampler.rate_limiter.last_tick = ts
    with mock.patch('async_jaeger.rate_limiter.RateLimiter.timestamp') \
            as mock_time:
        mock_time.side_effect = lambda: ts  # always return same time
        assert sampler.rate_limiter.timestamp() == ts
        sampled, _ = sampler.is_sampled(0)
        assert sampled, 'initial balance allows first item'
        sampled, _ = sampler.is_sampled(0)
        assert not sampled, 'initial balance exhausted'

        # move time 11s forward, enough credits to pay for one sample
        mock_time.side_effect = lambda: ts + 11
        sampled, _ = sampler.is_sampled(0)
        assert sampled
    sampler.close()
    assert '%s' % sampler == 'RateLimitingSampler(0.1)'

    # Test update
    sampler = RateLimitingSampler(3.0)
    sampler.rate_limiter.balance = 3.0
    ts = time.time()
    sampler.rate_limiter.last_tick = ts
    with mock.patch('async_jaeger.rate_limiter.RateLimiter.timestamp') \
            as mock_time:
        mock_time.side_effect = lambda: ts  # always return same time
        assert sampler.rate_limiter.timestamp() == ts
        sampled, _ = sampler.is_sampled(0)
        assert sampled
        assert sampler.rate_limiter.balance == 2.0
        assert '%s' % sampler == 'RateLimitingSampler(3.0)'

        sampler.update(3.0)
        assert '%s' % sampler == \
               'RateLimitingSampler(3.0)', 'should short cirtcuit if rate is the same'

        sampler.update(2.0)
        assert sampler.rate_limiter.balance == 4.0 / 3.0
        assert '%s' % sampler == 'RateLimitingSampler(2.0)'
    sampler.close()


def test_guaranteed_throughput_probabilistic_sampler():
    sampler = GuaranteedThroughputProbabilisticSampler('op',
                                                       2,
                                                       0.5)
    sampler.lower_bound_sampler.rate_limiter.balance = 2.0
    sampled, tags = sampler.is_sampled(MAX_INT - 10)
    assert sampled
    assert tags == get_tags('probabilistic', 0.5)
    sampled, tags = sampler.is_sampled(MAX_INT + 10)
    assert sampled
    assert tags == get_tags('lowerbound', 0.5)
    sampled, _ = sampler.is_sampled(MAX_INT + 10)
    assert not sampled
    assert '%s' % sampler == 'GuaranteedThroughputProbabilisticSampler(op, 0.500000, 2.000000)'

    sampler.update(3, 0.51)
    sampler.lower_bound_sampler.rate_limiter.balance = 3.0
    sampled, tags = sampler.is_sampled(MAX_INT - 10)
    assert sampled
    assert tags == get_tags('probabilistic', 0.51)
    sampled, tags = sampler.is_sampled(int(MAX_INT + (MAX_INT / 4)))
    assert sampled
    assert tags == get_tags('lowerbound', 0.51)

    assert '%s' % sampler == 'GuaranteedThroughputProbabilisticSampler(op, 0.510000, 3.000000)'
    sampler.close()


def test_adaptive_sampler():
    strategies = {
        'defaultSamplingProbability': 0.51,
        'defaultLowerBoundTracesPerSecond': 3,
        'perOperationStrategies':
        [
            {
                'operation': 'op',
                'probabilisticSampling': {
                    'samplingRate': 0.5
                }
            }
        ]
    }
    sampler = AdaptiveSampler(strategies, 2)
    sampled, tags = sampler.is_sampled(MAX_INT - 10, 'op')
    assert sampled
    assert tags == get_tags('probabilistic', 0.5)

    # This operation is seen for the first time by the sampler
    sampled, tags = sampler.is_sampled(MAX_INT - 10, 'new_op')
    assert sampled
    assert tags == get_tags('probabilistic', 0.51)

    ts = time.time()
    with mock.patch('async_jaeger.rate_limiter.RateLimiter.timestamp') \
            as mock_time:

        # Move time forward by a second to guarantee the rate limiter has enough credits
        mock_time.side_effect = lambda: ts + 1

        sampled, tags = sampler.is_sampled(int(MAX_INT + (MAX_INT / 4)), 'new_op')
        assert sampled
        assert tags == get_tags('lowerbound', 0.51)

    # This operation is seen for the first time by the sampler but surpasses
    # max_operations of 2. The default probabilistic sampler will be used
    sampled, tags = sampler.is_sampled(MAX_INT - 10, 'new_op_2')
    assert sampled
    assert tags == get_tags('probabilistic', 0.51)
    sampled, _ = sampler.is_sampled(int(MAX_INT + (MAX_INT / 4)), 'new_op_2')
    assert not sampled
    assert '%s' % sampler == 'AdaptiveSampler(0.510000, 3.000000, 2)'

    # Update the strategies
    strategies = {
        'defaultSamplingProbability': 0.52,
        'defaultLowerBoundTracesPerSecond': 4,
        'perOperationStrategies':
        [
            {
                'operation': 'op',
                'probabilisticSampling': {
                    'samplingRate': 0.52
                }
            },
            {
                'operation': 'new_op_3',
                'probabilisticSampling': {
                    'samplingRate': 0.53
                }
            }
        ]
    }
    sampler.update(strategies)

    # The probability for op has been updated
    sampled, tags = sampler.is_sampled(MAX_INT - 10, 'op')
    assert sampled
    assert tags == get_tags('probabilistic', 0.52)

    # A new operation has been added
    sampled, tags = sampler.is_sampled(MAX_INT - 10, 'new_op_3')
    assert sampled
    assert tags == get_tags('probabilistic', 0.53)
    assert '%s' % sampler == 'AdaptiveSampler(0.520000, 4.000000, 2)'

    sampler.close()


def test_adaptive_sampler_default_values():
    adaptive_sampler = AdaptiveSampler({}, 2)
    assert '%s' % adaptive_sampler == \
           'AdaptiveSampler(0.001000, 0.001667, 2)', 'sampler should use default values'

    sampled, tags = adaptive_sampler.is_sampled(0, 'op')
    assert sampled
    assert tags == \
        get_tags('probabilistic', 0.001), 'should use default probability'
    assert '%s' % adaptive_sampler.samplers['op'] == \
           'GuaranteedThroughputProbabilisticSampler(op, 0.001000, 0.001667)'

    adaptive_sampler.update(strategies={
        'defaultLowerBoundTracesPerSecond': 4,
        'perOperationStrategies':
            [
                {
                    'operation': 'new_op',
                    'probabilisticSampling': {
                        'samplingRate': 0.002
                    }
                }
            ]
    })
    assert '%s' % adaptive_sampler == 'AdaptiveSampler(0.001000, 4.000000, 2)'

    sampled, tags = adaptive_sampler.is_sampled(0, 'new_op')
    assert sampled
    assert tags == get_tags('probabilistic', 0.002)
    assert '%s' % adaptive_sampler.samplers['new_op'] == \
           'GuaranteedThroughputProbabilisticSampler(new_op, 0.002000, 4.000000)'

    sampled, tags = adaptive_sampler.is_sampled(0, 'op')
    assert sampled
    assert tags == get_tags('probabilistic', 0.001)
    # TODO ruh roh, the lowerbound isn't changed
    #  if the operation isn't included in perOperationStrategies
    assert '%s' % adaptive_sampler.samplers['op'] == \
           'GuaranteedThroughputProbabilisticSampler(op, 0.001000, 0.001667)'


def test_sampler_equality():
    const1 = ConstSampler(True)
    const2 = ConstSampler(True)
    const3 = ConstSampler(False)
    assert const1 == const2
    assert const1 != const3

    prob1 = ProbabilisticSampler(rate=0.01)
    prob2 = ProbabilisticSampler(rate=0.01)
    prob3 = ProbabilisticSampler(rate=0.02)
    assert prob1 == prob2
    assert prob1 != prob3
    assert const1 != prob1

    rate1 = RateLimitingSampler(max_traces_per_second=0.01)
    rate2 = RateLimitingSampler(max_traces_per_second=0.01)
    rate3 = RateLimitingSampler(max_traces_per_second=0.02)
    assert rate1 == rate2
    assert rate1 != rate3
    assert rate1 != const1
    assert rate1 != prob1


probabilistic_sampler = ProbabilisticSampler(0.002)
other_probabilistic_sampler = ProbabilisticSampler(0.003)
rate_limiting_sampler = RateLimitingSampler(10)
other_rate_limiting_sampler = RateLimitingSampler(20)


@pytest.mark.parametrize('strategy,expected', [
    ({'probabilisticSampling': {'samplingRate': 0.003}}, 0.003),
    ({}, 0.001),
    (None, 0.001),
    ({'probabilisticSampling': {}}, 0.001),
    ({'probabilisticSampling': None}, 0.001),
])
def test_get_sampling_probability(strategy, expected):
    assert expected == get_sampling_probability(strategy)


@pytest.mark.parametrize('strategy,expected', [
    ({'rateLimitingSampling': {'maxTracesPerSecond': 1}}, 1),
    ({}, 0.0016666),
    (None, 0.0016666),
    ({'rateLimitingSampling': {}}, 0.0016666),
    ({'rateLimitingSampling': None}, 0.0016666),
])
def test_get_rate_limit(strategy, expected):
    assert math.fabs(expected - get_rate_limit(strategy)) < 0.0001

from timer import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_timer():
    from timer import timer

    n = 1_000_000
    assert n * (n - 1) >> 1 == timer(sum)(range(n))

    import numpy as np

    numbers = np.arange(n)

    @timer
    def sum_numpy():
        return np.sum(numbers)

    sum_numpy()

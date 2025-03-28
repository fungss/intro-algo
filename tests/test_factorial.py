from src.factorial import factorial_iter, factorial_recur


def test_factorial_iter():
    expected_result = 120
    result = factorial_iter(5)
    assert result == expected_result


def test_factorial_recur():
    expected_result = 120
    result = factorial_recur(5)
    assert result == expected_result

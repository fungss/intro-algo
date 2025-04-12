from src.search import linear_search, binary_iter, binary_recur


def test_linear_search():
    expected_result = 4
    result = linear_search([2, 5, 8, 9, 10, 16, 22], 10)
    assert result == expected_result


def test_binary_iter():
    expected_result = 4
    result = binary_iter([2, 5, 8, 9, 10, 16, 22], 10)
    assert result == expected_result


def test_binary_recur():
    expected_result = 4
    arr = [2, 5, 8, 9, 10, 16, 22]
    result = binary_recur(arr, 0, len(arr)-1, 10)
    assert result == expected_result

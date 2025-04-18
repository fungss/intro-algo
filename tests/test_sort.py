from src.sort import bubble_sort, insertion_sort


def test_bubble_sort():
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert result == expected_result

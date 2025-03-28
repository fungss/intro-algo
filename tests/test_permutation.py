from src.permutation import permutation_iter, permutation_recur


def test_permutation_recur():
    expected_result = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    result = permutation_recur('ABC')
    assert result.sort() == expected_result.sort()

def permutation_iter(string: str) -> list:
    pass


def permutation_recur(string: str) -> list:
    if string == '':
        return []
    for idx, char in enumerate(string):
        sub_result = permutation_recur(string[:idx] + string[idx+1:])
        return [char + combo for combo in sub_result]

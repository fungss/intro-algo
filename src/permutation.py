"""Permutation done recursively and iteratively.

"""


def permutation_iter(string: str) -> list:
    """Return all possible permutations for a given string.

    The permutations are iteratively generated, follwing Heap's algorithm.

    Args:
        string: Any non-repeated random strings.

    Returns:
        A list of strings representing all possible permutations from 
            chars in the input.

    """
    results = []
    results.append(string)
    counters = [0] * len(string)

    i = 0
    while i < len(string):
        if counters[i] < i:
            if i % 2 == 0:
                # swap 0 and ith element if i even
                results.append(
                    string[i] + string[1:i] + string[0] + string[i+1:]
                )
            else:
                # swap counter[i] and ith element if i odd
                results.append(
                    string[:counters[i]]
                    + string[i]
                    + string[counters[i]+1:i]
                    + string[counters[i]]
                    + string[i+1:]
                )
            # increment counter[i] and reset i
            counters[i] += 1
            i = 0
        elif counters[i] == i:
            # reset counter[i] and increment i
            counters[i] = 0
            i += 1

    return results


def permutation_recur(string: str) -> list:
    if string == '':
        return []
    for idx, char in enumerate(string):
        sub_result = permutation_recur(string[:idx] + string[idx+1:])
        return [char + combo for combo in sub_result]

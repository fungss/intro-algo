"""Factorial done recursively and iteratively.

"""


def factorial_iter(num: int) -> int:
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def factorial_recur(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial_recur(num - 1)

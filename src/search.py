"""1 dimensional search algos

"""


def linear_search(arr, target):
    """return idx of target, -1 otherwise

    Not efficient if arr is large
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_iter(arr, target):
    """return idx of target, -1 otherwise

    Require arr to be sorted
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_recur(arr, start, end, target):
    """return idx of target, -1 otherwise

    Require arr to be sorted
    """
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_recur(arr, start, mid-1, target)
    elif arr[mid] < target:
        return binary_recur(arr, mid+1, end, target)

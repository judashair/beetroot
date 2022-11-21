def fib_search(arr, x, n):
    first = 0
    second = 1
    res = first + second
    while res < n:
        first = second
        second = res
        res = first + second
    offset = -1
    while res > 1:
        i = min(offset + first, n - 1)
        if arr[i] < x:
            res = second
            second = first
            first = res - second
            offset = i
        elif arr[i] > x:
            res = first
            second = second - first
            first = res - second
        else:
            return i
    if second and arr[offset + 1] == x:
        return offset + 1
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fib_search(array, 5, len(array) - 1))
print(fib_search(array, 1, len(array) - 1))
print(fib_search(array, 10, len(array) - 1))
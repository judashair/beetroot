def qsort(arr, ascending=True):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]

    if ascending:
        return qsort(less) + [pivot] + qsort(greater)
    else:
        return qsort(greater, ascending=False) + [pivot] + qsort(less, ascending=False)


numbers = [1, 2, 5, 6, 4, 9, 2, 10, -1, -5, 99, 4]

print(qsort(numbers, ascending = True))
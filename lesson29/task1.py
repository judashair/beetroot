def binary_search(item, sorted_collection):
    if len(sorted_collection) == 0:
        return False
    else:
        mid = len(sorted_collection) // 2
    if item == sorted_collection[mid]:
        return True
    else:
        if item < sorted_collection[mid]:
            return binary_search(item, sorted_collection[:mid])
        else:
            return binary_search(item, sorted_collection[mid + 1:])


collection = [i for i in range(101)]
print(binary_search(99, collection))
print(binary_search(120, collection))
print(binary_search(1, collection))
print(binary_search(0, collection))


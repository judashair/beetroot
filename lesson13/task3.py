def all_positive(nums: list):
    return all(map(lambda elem: elem > 0, nums))


def choose_func(nums: list, function_1, function_22):
    funcs = {True: function_1, False: function_22}
    return funcs.get(all_positive(nums))(nums)


def square_nums(nums: list):
    return [num ** 2 for num in nums]


def remove_negatives(nums: list):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
a = choose_func(nums1, square_nums, remove_negatives)
print(a)
b = choose_func(nums2, square_nums, remove_negatives)
print(b)
print(choose_func([], square_nums, remove_negatives))

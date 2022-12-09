def bubble_sort(nums, sort):
    n = True
    while n:
        n = False
        for i in range(len(nums) - 1):
            if sort == "up":
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    n = True
            if sort == "down":
                if nums[i + 1] > nums[i]:
                    nums[i + 1], nums[i] = nums[i], nums[i+1]
                    n = True


random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums, "up")
print(random_list_of_nums)


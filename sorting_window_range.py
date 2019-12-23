def min_window_to_sort(nums):
    lower_bound = upper_bound = -1
    max_num = -float('inf')
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
        if nums[i] < max_num:
            upper_bound = i
    min_num = float('inf')
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < min_num:
            min_num = nums[i]
        if nums[i] > min_num:
            lower_bound = i
    return (lower_bound, upper_bound)


print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
print(min_window_to_sort([2, 4, 5, 4, 7, 5, 6, 8, 9]))
# (2, 6)

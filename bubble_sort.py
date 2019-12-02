def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1],  nums[j]
        print(nums)
    return nums


print(bubble_sort([4, 1, 0, 3, 5, 1, 2, 6]))

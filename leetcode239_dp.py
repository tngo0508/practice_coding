def maxSlidingWindow(nums):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    left = nums * [0]
    left[0] = nums[0]
    right = nums * [0]
    right[n - 1] = nums[n - 1]

    for i in range(1, n):
        if i % k == 0:
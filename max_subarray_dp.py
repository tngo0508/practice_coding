def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    res = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        res = max(nums[i], res)
    return res


print(maxSubArray([-1]))
# -1
print(maxSubArray([-2, -1]))
# -1
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# 6
print(maxSubArray([1]))
# 1
print(maxSubArray([-2, 1]))
# 1

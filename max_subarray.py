def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return []
    current_max = res = nums[0]

    for num in nums[1:]:
        # current_max = current_max + num
        # if current_max < num:
        #     current_max = num
        # if current_max > res:
        #     res = current_max

        current_max = max(num, current_max + num)
        res = max(current_max, res)

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

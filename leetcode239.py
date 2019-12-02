# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # res = []
    # for i in range((len(nums) - k + 1)):
    #     res.append(max(nums[i:i+k]))

    # return res
    if len(nums) == 0:
        return []
    return [max(nums[i:i + k]) for i in range((len(nums) - k + 1))]


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

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
from collections import deque


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    def clean_deque(i):
        if d and d[0] == i - k:
            d.popleft

        while d and nums[i] > nums[d[-1]]:
            d.pop()

    d = deque()
    max_idx = 0
    for i in range(k):
        clean_deque(i)
        d.append(i)
        if nums[i] > nums[max_idx]:
            max_idx = i

    output = [nums[max_idx]]

    for i in range(k, n):
        clean_deque(i)
        d.append(i)
        output.append(nums[d[0]])
    return output


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

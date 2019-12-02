import heapq


def findKthLargest(nums, k):
    heapq.heapify(nums)
    return nums[-k]

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5

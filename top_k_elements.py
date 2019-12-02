import heapq


class Solution:
    def topKElement(self, nums, k):
        return heapq.nlargest(k, nums)


print(Solution().topKElement([1, 1, 1, 2, 2, 3, 3], 2))
#[1, 2]
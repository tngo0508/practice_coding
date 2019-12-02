class Solution:
    def minSubArrayLen(self, nums, s):
        l, r = 0, -1
        sum = 0
        res = len(nums) + 1

        while l < len(nums):
            if sum < s and r + 1 < len(nums):
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1

            if sum >= s:
                res = min(res, r - l + 1)

        if res == len(nums) + 1:
            return 0
        return res


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
print(Solution().minSubArrayLen([0, 0, 1], 7))
# 0

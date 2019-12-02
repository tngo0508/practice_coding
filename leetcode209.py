class Solution:
    def minSubArrayLen(self, nums, s):
        l, r = 0, -1
        sum = 0
        res = len(nums) + 1
        while(l < len(nums)):
            if (sum < s) and (r + 1 < len(nums)):
                # if sum is smaller, keep moving right index to increase window
                r += 1
                sum += nums[r]
            else:
                # if sum >= s, move left index to shrink window
                sum -= nums[l]
                l += 1

            if sum >= s:
                # if sum is found
                res = min(res, r - l + 1)
        if(res == len(nums) + 1):
            # if no solution is found
            return 0
        return res


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
print(Solution().minSubArrayLen([0, 0, 0], 7))
# 0

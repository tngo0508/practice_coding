class Solution:
    def permutate(self, nums):
        res = []
        def permutateHelper(start):
            if start == len(nums) - 1:
                res.append(nums[:])

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permutateHelper(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
            return res
        return permutateHelper(0)


print(Solution().permutate([1, 2, 3]))

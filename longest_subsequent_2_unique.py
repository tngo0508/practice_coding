class Solution:
    def longest_2_unique(self, nums):
        if len(nums) <= 2:
            return len(nums)
        unique = []
        i, k = 0, 1
        unique.append(nums[i])
        if nums[i] != nums[k]:
            unique.append(nums[k])
        max_length = 2
        while k < len(nums):
            if len(unique) < 2 and nums[i] != nums[k]:
                    unique.append(nums[k])
            if nums[k] in unique:
                max_length = max(max_length, k - i + 1)
                k += 1
            else:
                i += 1
                k = i + 1
                unique = []
                if nums[i] == nums[k]:
                    unique.append(nums[i])
                else:
                    unique.append(nums[i])
                    unique.append(nums[k])
        return max_length

print(Solution().longest_2_unique([1, 3, 5, 3, 1, 3, 1, 5]))
print(Solution().longest_2_unique([1, 1, 3]))
print(Solution().longest_2_unique([1, 2, 1, 3, 3, 3]))
print(Solution().longest_2_unique([1, 1, 2, 2, 3, 3, 3]))
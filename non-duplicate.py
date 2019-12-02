class Solution:
    def singleNumber(self, nums):
        occurence = {}
        for n in nums:
            occurence[n] = occurence.get(n, 0) + 1

        for key, value in occurence.items():
            if value == 1:
                return key
    
    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
            print(unique)
        return unique


print(Solution().singleNumber2([4, 3, 2, 4, 1, 3, 2]))
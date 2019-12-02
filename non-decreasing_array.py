class Solution:
    def checkPossibility(self, nums):
        idx = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # if there are two dips or mroe
                if idx is not None:
                    return False
                idx = i
        # there is no dip
        if idx is None:
            return True
        # there is only one dip
        if idx == 0:
            return True
        if idx == len(nums) - 2:
            return True
        if nums[idx] <= nums[idx + 2]:
            return True
        if nums[idx - 1] <= nums[idx + 1]:
            return True
        return False

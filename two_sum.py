from collections import defaultdict


def twoSum(nums, target):
    d = defaultdict()

    for i in range(len(nums)):
        comp = target - nums[i]

        if comp in d:
            return [d[comp], i]

        d[nums[i]] = i
    print d
    return -1


print twoSum([2, 7, 11, 15], 9)
# [0, 1]

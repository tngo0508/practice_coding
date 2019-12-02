import collections


def sortNums(nums):
    count = collections.Counter(nums)
    return [1] * count[1] + [2] * count[2] + [3] * count[3]

def sortNums2(nums):
    one_index = 0
    three_index = len(nums) - 1
    index = 0
    while index <= three_index:
        if nums[index] == 1:
            nums[index], nums[one_index] = nums[one_index], nums[index]
            one_index += 1
            index += 1
        elif nums[index] == 2:
            index += 1
        elif nums[index] == 3:
            nums[index], nums[three_index] = nums[three_index], nums[index]
            three_index -= 1
    return nums
print(sortNums2([3, 3, 2, 1, 3, 2, 1]))

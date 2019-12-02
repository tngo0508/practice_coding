
def cross_sum(nums, left, right, p):
    if left == right:
        return nums[left]

    left_subsum = float('-inf')
    curr_sum = 0

    # for i in range(p, left - 1, -1):
    for i in range(left, p + 1):
        curr_sum += nums[i]
        left_subsum = max(left_subsum, curr_sum)
        print(p, curr_sum, left_subsum)

    right_subsum = float('-inf')
    curr_sum = 0
    for i in range(p + 1, right + 1):
        curr_sum += nums[i]
        right_subsum = max(right_subsum, curr_sum)

    return left_subsum + right_subsum


def helper(nums, left, right):
    if left == right:
        return nums[left]

    p = (left + right) // 2
    # print(p)

    left_sum = helper(nums, left, p)
    right_sum = helper(nums, p + 1, right)
    cross_sum_ = cross_sum(nums, left, right, p)

    return max(left_sum, right_sum, cross_sum_)


def maxSubArray(nums: 'List[int]') -> 'int':
    return helper(nums, 0, len(nums) - 1)


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# 6 <- [4, -1, 2, 1]

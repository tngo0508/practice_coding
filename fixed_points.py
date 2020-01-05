def find_fixed_point(nums):
    return binary_search(0, len(nums), nums)


def binary_search(lo, hi, nums):
    if lo == hi:
        return None
    mid = lo + (hi - lo) // 2
    if nums[mid] == mid:
        return mid
    elif nums[mid] < mid:
        return binary_search(mid + 1, hi, nums)
    return binary_search(lo, mid, nums)


print(find_fixed_point([-5, 1, 3, 4]))
# 1

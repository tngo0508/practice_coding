def binary_search_iterative(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def binary_search(nums, target):
    return helper(nums, 0, len(nums) - 1, target)

def helper(nums, lo, hi, target):
    if hi < lo:
        return False
    mid = lo + (hi - lo) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        return helper(nums, lo, mid - 1, target)
    else:
        return helper(nums, mid + 1, hi, target)

print(binary_search([1,2,2,3,4,5,5,5,6], 0))
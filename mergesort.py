def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    p = int((len(nums) / 2))
    left = merge_sort(nums[:p])
    right = merge_sort(nums[p:])
    return merge(left, right)


def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


print(merge_sort([1, 5, 3, 2, 8, 7, 6, 4]))

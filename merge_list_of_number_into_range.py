def find_range(nums):
    res = []
    i = j = k = 0
    while k < len(nums):
        diff = nums[k] - nums[j]
        if diff <= 1:
            j += 1
        else:
            res.append((nums[i], nums[j]))
            i = j = k
        k = j + 1
    res.append((nums[i], nums[j]))
    return res


# techlead solution
def makerange(low, high):
    return str(low) + '-' + str(high)


def findRanges(nums):
    if not nums:
        return []

    ranges = []
    low = nums[0]
    high = nums[0]

    for n in nums:
        if high + 1 < n:
            ranges.append(makerange(low, high))
            low = n
        high = n
    ranges.append(makerange(low, high))
    return ranges


print(find_range([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# [0,2], [5], [7,11], [15]

def permute(nums):
    if (len(nums) == 1):
        return [nums]

    output = []
    for l in permute(nums[1:]):
        for idx in range(len(nums)):
            output.append(l[:idx] + [nums[0]] + l[idx:])

    return output


print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

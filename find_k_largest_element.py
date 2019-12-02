import random


def findKthLargest(nums, k):
    def quick_select(lst, l, r, idx):
        if r == l:
            return lst[l]

        pivot_idx = random.randint(l, r)

        # move pivot to the beginning of list
        lst[l], lst[pivot_idx] = lst[pivot_idx], lst[l]

        # partition
        i = l
        for j in range(l + 1, r + 1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]

        # recursively parition one side only
        if idx == i:
            return lst[i]
        elif idx < i:
            return quick_select(lst, l, i - 1, idx)
        else:
            return quick_select(lst, i + 1, r, idx)

    return quick_select(nums, 0, len(nums) - 1, k)


print(findKthLargest([3, 5, 2, 4, 6, 8], 9))

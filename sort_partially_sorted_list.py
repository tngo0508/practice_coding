import heapq


def sort_partially_sorted(nums, k):
    heap = []
    res = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) == 3:
            res.append(heapq.heappop(heap))
    while heap:
        res.append(heapq.heappop(heap))
    return res


print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]

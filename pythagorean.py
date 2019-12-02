import time


start_time = time.time()


def findPythagoreanTriplets(nums):
    # Fill this in.
    tmp = set([x ** 2 for x in nums])
    # tmp = ([x ** 2 for x in nums])
    for x in nums:
        for y in nums:
            if x**2 + y**2 in tmp:
                return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
end_time = time.time()
print((end_time - start_time) * 1000)

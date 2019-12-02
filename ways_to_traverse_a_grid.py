def num_ways(n, m):
    if n == 1 or m == 1:
        return 1

    return num_ways(n - 1, m) + num_ways(n, m - 1)


print(num_ways(2, 2))
# 2

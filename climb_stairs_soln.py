def staircase(n):
    # Fill this in.
    res = [0 for x in range(0, n+1)]
    res[0] = res[1] = 1
    for i in range(2, n+1):
        j = 1
        while j <= 2 and j <= i:
            res[i] = res[i] + res[i - j]
            print(j, i, res[i])
            j = j + 1
    return res[n]


print(staircase(4))
# 5
print(staircase(5))
# 8

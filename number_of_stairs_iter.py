def staircase(n):
    # Fill this in.
    arr = [0] * (n+1)
    arr[0] = arr[1] = 1
    i = 2
    while i <= n:
        arr[i] = arr[i - 1] + arr[i - 2]
        i += 1
    return arr[n]


print staircase(4)
# 5
print staircase(5)
# 8

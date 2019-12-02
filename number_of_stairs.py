def staircase(n):
    # Fill this in.
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)


print staircase(4)
# 5
print staircase(5)
# 8
print staircase(2)
def reverse_digit(x):
    res, remaining_x = 0, abs(x)
    while remaining_x:
        res = res * 10 + remaining_x % 10
        remaining_x //= 10
    return -res if x < 0 else res

print(reverse_digit(24))
# 42

print(reverse_digit(-123))
# -321
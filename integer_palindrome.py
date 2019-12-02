import math

def check_palindrome(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    print(msd_mask)
    print(122 % 100)
    for _ in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


print(check_palindrome(2147447412))
# True
print(check_palindrome(333))
# True
print(check_palindrome(-100))
# False
print(check_palindrome(12))
# False

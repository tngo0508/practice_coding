KAPREKAR_CONSTANT = 6174


def num_kaprekar_iterations(n):
    count = 0
    while n != KAPREKAR_CONSTANT:
        asc_n = int(''.join(sorted(list(str(n)))))

        des_n = 0
        while n:
            r = n % 10
            n = n // 10
            des_n = des_n * 10 + r
        rev_str = sorted(list(str(des_n)), reverse=True)
        if len(rev_str) < 4:
            rev_str.append('0')
        des_n = int(''.join(rev_str))
        n = des_n - asc_n
        count += 1
    return count


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)

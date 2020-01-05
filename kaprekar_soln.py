KAPREKAR_CONSTANT = 6174


def num_kaprekar_iterations(n):
    if n == KAPREKAR_CONSTANT:
        return 0
    n_str = str(n)
    asc_num = int(''.join(sorted(n_str)))
    desc_str = sorted(n_str, reverse=True)
    desc_str = desc_str + ['0'] * (4 - len(desc_str))
    desc_num = int(''.join(desc_str))
    new_num = desc_num - asc_num
    return 1 + num_kaprekar_iterations(new_num)


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)

def distance(s1, s2):
    # Fill this in.
    x = len(s1) + 1
    y = len(s2) + 1

    A = [[-1 for i in range(x)] for j in range(y)]

    for i in range(x):
        A[0][i] = i
    for j in range(y):
        A[j][0] = j

    for i in range(1, y):
        for j in range(1, x):
            if s1[j - 1] == s2[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                    A[i - 1][j] + 1,
                    A[i - 1][j - 1] + 1,
                    A[i][j - 1] + 1
                )
            # print A[i - 1][j] + 1, A[i - 1][j - 1] + \
            #     1, A[i][j - 1] + 1, A[i][j]
    # print A[i][j]
    return A[y - 1][x - 1]


print distance('biting', 'sitting')
# 2
print distance('intention', 'execution')
# 5
print distance('abc', 'def')

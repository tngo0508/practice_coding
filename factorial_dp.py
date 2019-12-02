def factorial(n):
    A = [0] * (n + 1)
    A[0] = A[1] = 1
    for i in range(2, n + 1):
        A[i] = A[i-1] * i
    print(A)
    return A[n]


print(factorial(3))
print(factorial(4))
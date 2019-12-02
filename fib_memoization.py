def fib(n):
    def fib_memo(n, memo):
        if n in memo:
            return memo[n]

        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]
    
    memo = {1: 1, 2: 1}
    return fib_memo(n, memo)

print(fib(100))
def fibonacci(n, memo):
    result = 0
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        result = 1

    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    memo[n] = result
    return result


n = int(input())
d = dict()
print(fibonacci(n, d))

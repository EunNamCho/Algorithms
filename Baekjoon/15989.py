T = int(input())
tests = [int(input()) for _ in range(T)]

max_n = max(tests)
dp = [0] * (max_n + 1)
dp[0] = 1

for coin in [1, 2, 3]:
    for i in range(coin, max_n + 1):
        dp[i] += dp[i - coin]

for n in tests:
    print(dp[n])

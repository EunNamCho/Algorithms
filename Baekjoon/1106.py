import sys
input = sys.stdin.readline

def main():
    C, N = map(int, input().split())
    cities = [tuple(map(int, input().split())) for _ in range(N)]  # (cost, gain)

    max_gain = max(gain for cost, gain in cities)
    INF = float('inf')

    dp = [INF] * (C + max_gain + 1)
    dp[0] = 0

    for cost, gain in cities:
        for x in range(gain, C + max_gain + 1):
            dp[x] = min(dp[x], dp[x - gain] + cost)

    print(min(dp[C:]))

main()
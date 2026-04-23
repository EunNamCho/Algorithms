import sys
input = sys.stdin.readline


def main():
    # Input
    N, K = map(int, input().split())
    weights, values = [], []
    for _ in range(N):
        weight, value = map(int, input().split())
        weights.append(weight)
        values.append(value)
        
    # Algorithm - DP
    dp = [0] * (K+1)
    for n in range(N):
        W = weights[n]
        for w in range(K,W-1,-1):
            dp[w] = max(dp[w], values[n]+dp[w-weights[n]])
        # print(dp)
    print(dp[K])
    
main()
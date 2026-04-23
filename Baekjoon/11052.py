import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    prices = list(map(int,input().split()))
    
    # Algorithm - DP
    dp = [[0]*N for _ in range(N)]
    dp[0] = [i*prices[0] for i in range(1,N+1)]
    
    for i in range(1,N):
        for j in range(N):
            if j>i:
                dp[i][j] = max(dp[i-1][j], dp[i][j-i-1]+prices[i])
            elif j==i:
                dp[i][j] = max(dp[i-1][j],prices[i])
            else:
                dp[i][j] = dp[i-1][j]
    
    # for row in dp:
    #     print(*row)
    print(dp[N-1][N-1])

main()
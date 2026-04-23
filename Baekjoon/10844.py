import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    
    # Algorithm - DP
    dp = [[1]*10, [1]*10]
    dp[0][0]=0
    dp[1][0]=0
    for _ in range(1,N):
        for i in range(10):
            if i==0:
                dp[1][i] = (dp[0][i+1])%1_000_000_000
            elif i==9:
                dp[1][i] = (dp[0][i-1])%1_000_000_000
            else:
                dp[1][i] = (dp[0][i-1]+dp[0][i+1])%1_000_000_000
        for i in range(10):
            dp[0][i] = dp[1][i]
            
    print(sum(dp[1])%1_000_000_000)

main()
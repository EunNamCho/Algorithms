import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    
    # Algorithm - DP
    dp = [[0,1],[0,1]]
    for _ in range(1,N):
        dp[1][0] = dp[0][0]+dp[0][1]
        dp[1][1] = dp[0][0]
        
        dp[0][0] = dp[1][0]
        dp[0][1] = dp[1][1]
        
    print(sum(dp[1]))

main()
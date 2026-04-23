import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    
    # Algorithm - DP
    dp = [1]*10
    for i in range(1,N):
        for j in range(9,-1,-1):
            for k in range(j-1,-1,-1):
                dp[j]=(dp[j]+dp[k])%10007
    # print(dp)
    print(sum(dp)%10007)

main()
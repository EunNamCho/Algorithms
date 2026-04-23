import sys
input = sys.stdin.readline

def main():
    # Input
    A = input().rstrip()
    B = input().rstrip()
    
    # Algorithm - LCS
    dp = [[0]*(len(B)+1) for _ in range((len(A)+1))]
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a==b:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # for row in dp:
    #     print(row)
    print(dp[len(A)][len(B)])
    
main()
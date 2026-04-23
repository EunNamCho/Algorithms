import sys
input = sys.stdin.readline

def main():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        sticker = [list(map(int, input().split())),
                   list(map(int, input().split()))]
        
        if n == 1:
            print(max(sticker[0][0], sticker[1][0]))
            continue
        
        # dp 배열
        dp = [[0] * n for _ in range(2)]
        
        # 초기값
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]
        
        # 점화식
        for i in range(2, n):
            dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
        
        print(max(dp[0][n-1], dp[1][n-1]))

main()

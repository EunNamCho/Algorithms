import sys
input = sys.stdin.readline

def main():
    # Input
    N,K = map(int,input().split())
    coins = set()
    for _ in range(N):
        coins.add(int(input()))
    coins = list(coins)
    N = len(coins)
        
    # Algorithm - DP
    dp = [[float('inf')]*(K+1) for _ in range(N)]
    coin = coins[0]
    for i in range(N):
        dp[i][0] = 0
    for i in range(1,K+1):
        q,r = divmod(i,coin)
        if r==0:
            dp[0][i]=q

    for i in range(1,N):
        coin = coins[i]
        # print(coin)
        for j in range(1,K+1):
            if j>=coin:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-coin]+1)
            else:
                dp[i][j] = dp[i-1][j]
                
    # for row in dp:
    #     print(*row)
    answer = dp[N-1][K]
    if answer==float('inf'):
        answer=-1
    print(answer)
    
main()
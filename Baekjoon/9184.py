import sys

dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
while True:
    # input
    a, b, c= map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break

    # algorithm - DP
    def w(a,b,c):
        if a<=0 or b<=0 or c<=0:
            dp[a][b][c] = 1
            return dp[a][b][c]
        if a>20 or b>20 or c>20:
            dp[a][b][c] = w(20,20,20)
            return dp[a][b][c]
        if dp[a][b][c]>1:
            return dp[a][b][c]
        if a<b<c:
            dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1)-w(a,b-1,c)
        else:
            dp[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return dp[a][b][c]
    w(a,b,c)
    print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")

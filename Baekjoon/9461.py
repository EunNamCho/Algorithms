import sys
input = sys.stdin.readline
write = sys.stdout.write

# Input
T = int(input())
outputs = []

# Algorithm - DP
dp = [0]*101
dp[1],dp[2],dp[3],dp[4],dp[5],dp[6] = 1,1,1,2,2,3
for _ in range(T):
    n = int(input())
    for i in range(1,n+1):
        if dp[i]==0:
            dp[i] = dp[i-1]+dp[i-5]
    outputs.append(str(dp[n]))

write("\n".join(outputs))        
    
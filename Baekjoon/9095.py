import sys
input = sys.stdin.readline
write = sys.stdout.write

# Input
T = int(input())
outputs = []

# Algorithm - DP
dp = [0]*12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n = int(input())
    for i in range(1,n+1):
        if dp[i]==0:
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    outputs.append(dp[n])
    
write("\n".join(map(str,outputs)))
    
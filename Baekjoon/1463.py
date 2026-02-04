import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

# Input
N = int(input())
answer = float("inf")

# Algorithm - BackTracking(BFS)
operations = ["2", "3", "1"]
queue = deque([(N,0)])
distances = {N: 0}

while queue:
    n, depth = queue.pop()
    # print(n,depth)
    
    if depth > answer: 
        continue
    if n==1 and depth < answer: 
        answer = depth
        
    for operation in operations:
        if operation=="2":
            if n%2==0 and (distances.get(n//2) is None or  distances.get(n//2) > depth+1):
                # print("2", n,depth)
                distances[n//2] = depth+1
                queue.appendleft((n//2, depth+1))
        elif operation=="3":
            if n%3==0 and (distances.get(n//3) is None or distances.get(n//3) > depth+1):
                # print("3", n,depth)
                distances[n//3] = depth+1
                queue.appendleft((n//3, depth+1))
        elif operation=="1":
            if distances.get(n-1) is None or distances.get(n-1) > depth+1:
                # print("1", n,depth)
                distances[n-1] = depth+1
                queue.appendleft((n-1, depth+1))
                
print(answer)



########## DP로 풀수도 있지만, 이 문제에서는 시간이 더 오래 걸림.
import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)

for x in range(2, N + 1):
    dp[x] = dp[x - 1] + 1
    if x % 2 == 0:
        dp[x] = min(dp[x], dp[x // 2] + 1)
    if x % 3 == 0:
        dp[x] = min(dp[x], dp[x // 3] + 1)

print(dp[N])

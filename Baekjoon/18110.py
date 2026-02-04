import sys
from collections import deque

# input
N = int(sys.stdin.readline())
rates = []
for _ in range(N):
    rate = int(sys.stdin.readline())
    rates.append(rate)

# Algorithm - Implementation
def my_round(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    else:
        return int(x)
    
rates = deque(sorted(rates))
percentile = my_round(N*0.15)

cnt = 0
while rates:
    if cnt==percentile:
        break
    rates.pop()
    cnt+=1
    
cnt = 0
while rates:
    if cnt==percentile:
        break
    rates.popleft()
    cnt+=1
    
if len(rates)>0:
    answer = my_round(sum(rates)/len(rates))
else:
    answer = 0
print(answer)


import sys

# input
N = int(sys.stdin.readline())
rates = [int(sys.stdin.readline()) for _ in range(N)]

if N == 0:
    print(0)
    sys.exit()

# Algorithm - Implementation
def my_round(x):
    return int(x + 0.5)

rates.sort()
k = my_round(N * 0.15)

L = k
R = N - k - 1

if L > R:
    print(0)
else:
    total = 0
    for i in range(L, R + 1):
        total += rates[i]
    answer = my_round(total / (R - L + 1))
    print(answer)

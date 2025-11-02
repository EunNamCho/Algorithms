import sys
import math

# input
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
B, C = map(int, sys.stdin.readline().strip().split())
answer = 0

# algorithm - Implementation
for a in A:
    a-=B
    answer += 1
    if a<=0:
        continue
    answer += math.ceil(a/C)


print(answer)
# 6M
import sys

# input
N,M = map(int, sys.stdin.readline().split())

# algorithm - Backtracking
def back(start, combination):
    if len(combination)==M:
        print(" ".join(combination))
        return
    
    for i in range(start,N+1):
        combination.append(str(i))
        back(i, combination)
        combination.pop()

back(1,[])
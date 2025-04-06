# 5M
import sys

# input
N,M = map(int, sys.stdin.readline().split())

# algorithm - Backtracking
def back(combination):
    if len(combination)==M:
        print(" ".join(combination))
        return 
    
    for i in range(1,N+1):
        combination.append(str(i))
        back(combination)
        combination.pop()

back([])
import sys
from collections import defaultdict

# input
N,M = map(int, sys.stdin.readline().strip().split())
numbers = list(range(1,N+1))
# visited = [0]*(N+1)

# algorithm - Backtracking
def back(start, length,combination):
    if length==0:
        # print(" ".join(map(str,combination)))
        print(*combination)
    
    for number in numbers[start:]:
        # if not visited[number]:
        # combination.append(number)
        # visited[number] = 1
        back(number,length-1,combination+[number])
        # combination.pop()
        # visited[number] = 0

back(0,M,[])

# output
# for combination in answer.keys():
#     print(combination)
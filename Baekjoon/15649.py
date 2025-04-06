# 26M
# 핵심은 visited로 검사
# length==0일 때, 출력.
import sys

# input
N,M = map(int, sys.stdin.readline().strip().split())
numbers = list(range(1,N+1))
visited = [0] * (N+1)
answer = []

# algorithm - Backtracking
def back(length, combination):
    if length==0:
        # output
        print(" ".join(map(str,combination)))
        return
    
    for number in numbers:
        if not visited[number]:
            combination.append(number)
            visited[number] = 1
            back(length-1, combination)
            combination.pop()
            visited[number] = 0

back(M,[])

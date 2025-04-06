# 50분... list로 adjacent matrix 구현하니까, 메모리초과 뜸.
import sys
from collections import defaultdict
import heapq
sys.setrecursionlimit(100000000)

# input
N, M, R = map(int, sys.stdin.readline().strip().split())
matrix = defaultdict(list)
visited = [0]*N
step = [1]

for _ in range(M):
    src, dst = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(matrix[src-1], dst-1)
    heapq.heappush(matrix[dst-1], src-1)
visited[R-1] = 1

# input check
# for row in matrix:
#     print(row)
# print(visited)

# algorithm - DFS
def iter_dfs(start):
    while matrix[start]:
        dst = heapq.heappop(matrix[start])
        if not visited[dst]:
            dfs(dst)

def dfs(src):
    step[0] += 1
    visited[src] = step[0]
    while matrix[src]:
        dst = heapq.heappop(matrix[src])
        if not visited[dst]:
            dfs(dst)

iter_dfs(R-1)

# output
for v in visited:
    print(v)
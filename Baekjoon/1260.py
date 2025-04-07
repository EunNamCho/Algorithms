# 18분

import sys
from collections import deque
sys.setrecursionlimit(100000000)

# input
N, M, V = map(int, sys.stdin.readline().strip().split())
matrix_dfs = [[0]*N for _ in range(N)]
matrix_bfs = [[0]*N for _ in range(N)]
answer_dfs = [V]
answer_bfs = [V]
queue = deque([V-1])
visited = [False]*N
for _ in range(M):
    src, dst = map(lambda x:x-1,map(int, sys.stdin.readline().strip().split()))
    matrix_dfs[src][dst] = 1
    matrix_dfs[dst][src] = 1
    matrix_bfs[src][dst] = 1
    matrix_bfs[dst][src] = 1

# input check
# for row in matrix_dfs:
#     print(row)

# algorithm - DFS
def iter_dfs(y):
    for x, _ in enumerate(matrix_dfs[y]):
        if matrix_dfs[y][x]==1 and not visited[x]:
            visited[y] = True
            dfs(y, x)

def dfs(src, dst):
    visited[dst] = True
    answer_dfs.append(dst+1)
    for x, _ in enumerate(matrix_dfs[dst]):
        if matrix_dfs[dst][x]==1 and not visited[x]:
            dfs(dst, x)

iter_dfs(V-1)
visited = [False]*N

# algorithm - BFS
visited[V-1] = True
while queue:
    src = queue.popleft()
    for dst, _ in enumerate(matrix_bfs[src]):
        if matrix_dfs[src][dst]==1 and not visited[dst]:
            visited[dst] = True
            queue.append(dst)
            answer_bfs.append(dst+1)

for t in answer_dfs:
    print(t, end= " ")
print()
for t in answer_bfs:
    print(t, end=" ")

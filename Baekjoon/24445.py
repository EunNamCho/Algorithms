# 8분
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10000000)

# input
N,M,R = map(int, sys.stdin.readline().strip().split())
matrix = defaultdict(list)
visited = [0]*N
visited[R-1] = 1
step = 1
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(matrix[src-1], -(dst-1))
    heapq.heappush(matrix[dst-1], -(src-1))

# algorithm - BFS
queue = deque([R-1])
while queue:
    src = queue.popleft()
    while matrix[src]:
        dst = -heapq.heappop(matrix[src])
        if not visited[dst]:
            step += 1
            visited[dst] = step
            queue.append(dst)

# output
for v in visited:
    print(v)
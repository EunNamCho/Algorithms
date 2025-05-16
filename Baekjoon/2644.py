#15M
import sys
from collections import defaultdict, deque

# input
N = int(sys.stdin.readline())
queue = deque()
visited = [-1] * (N+1)
src, dst = map(int, sys.stdin.readline().split())
matrix = defaultdict(list)
for _ in range(int(sys.stdin.readline())):
    x, y = map(int,sys.stdin.readline().split())
    matrix[y].append(x)
    matrix[x].append(y)

# input check
# for k,v in matrix.items():
#     print(k,":",v)

# algorithm - BFS
queue.append(src)
visited[src] = 0
while queue:
    cur = queue.popleft()
    # print(visited)
    if cur==dst:
        print(visited[cur])
        sys.exit()
    for neighbor in matrix[cur]:
        if visited[neighbor]==-1:
            queue.append(neighbor)
            visited[neighbor] = visited[cur]+1

print(visited[dst])
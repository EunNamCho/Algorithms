import sys
from collections import defaultdict, deque
import heapq

# input
N,K = map(int, sys.stdin.readline().strip().split())
visited = [0]*100_001

# algorithm - BFS
queue = deque([N])
while queue:
    cur = queue.popleft()
    neighbors = [cur-1, cur+1, cur*2]
    if cur==K:
        break
    for neighbor in neighbors:
        if 0<=neighbor<100_001 and not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = visited[cur] + 1

# output
print(visited[K])
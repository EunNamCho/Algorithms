import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Algorithm - DFS
component = 0
visited = [False]*(N+1)

for i in range(1,N+1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True
        component += 1
    while queue:
        u = queue.popleft()
        for neighbor in graph[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

print(component)
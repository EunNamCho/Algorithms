import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# input
N, Q = map(int, input().split())
graph = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

# algorithm
answers = []
for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    queue = deque([v])
    visited[v] = True
    count = 0

    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if not visited[neighbor] and weight >= k:
                visited[neighbor] = True  # ✅ fix 위치
                count += 1
                queue.append(neighbor)
    
    answers.append(str(count))

# output
print("\n".join(answers))

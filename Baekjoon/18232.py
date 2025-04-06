# 이거 dirs로 다시 한 번 풀어야함. 시간 너무 오래 걸림
import sys
from collections import defaultdict, deque
import heapq

# input
N,M = map(int, sys.stdin.readline().strip().split())
S,E = map(int, sys.stdin.readline().strip().split())
visited = [0]*(N+1)
matrix = defaultdict(list)
dirs = [-1,1]
# for vertex in range(1,N+1):
#     for dir in [-1,1]:
#         neighbor = vertex+dir
#         if 1<=neighbor<N+1:
#             if neighbor not in matrix[vertex]: 
#                 heapq.heappush(matrix[vertex],neighbor)
#             if vertex not in matrix[neighbor]:
#                 heapq.heappush(matrix[neighbor],vertex)

# input check
# print("============")
# for k,v in matrix.items():
#     print(k,v)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    # if y not in matrix[x]: 이거 없애니까 시간 줄어듦듦
    heapq.heappush(matrix[x],y)
    # matrix[x].append(y)
    # if x not in matrix[y]:
    heapq.heappush(matrix[y],x)
    # matrix[y].append(x)

# input check
# for k,v in matrix.items():
#     print(k,v)

# algorithm - BFS
queue = deque([S])
while queue:
    cur = queue.popleft()
    if cur==E:
            break
    while matrix[cur]:
        neighbor = heapq.heappop(matrix[cur])
        # neighbor = matrix[cur].pop()
        if not visited[neighbor]:
            visited[neighbor] = visited[cur]+1
            queue.append(neighbor)
    for dx in dirs:
        neighbor = dx + cur
        if 1<=neighbor<N+1:
            if not visited[neighbor]:
                visited[neighbor] = visited[cur]+1
                queue.append(neighbor)

# output
print(visited[E])
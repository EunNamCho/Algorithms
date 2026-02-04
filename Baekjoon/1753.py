import sys
import heapq
from collections import defaultdict

# input
V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
matrix = defaultdict(list)
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    matrix[u].append((v,w))

# Algorithm - Daikstra
dists = [float("inf")]*(V+1)
dists[K] = 0
pq = []
heapq.heappush(pq,(0,K))

while pq:
    dist, u = heapq.heappop(pq)
    if dist > dists[u]:
        continue
    
    for neighbor, cost in matrix[u]:
        if dists[neighbor] > cost + dists[u]:
            dists[neighbor] = cost + dists[u]
            heapq.heappush(pq, (dists[neighbor],neighbor))

for idx in range(1,V+1):
    dist = dists[idx]
    if dist==float("inf"):
        print("INF")
    else:
        print(dist)

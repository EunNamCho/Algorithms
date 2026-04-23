import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    start, end = map(int, input().split())
    
    INF = 10**15
    dist = [INF] * (N + 1)
    dist[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > dist[node]:
            continue
        
        if node == end:
            break
        
        for nxt, w in graph[node]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    
    print(dist[end])

main()

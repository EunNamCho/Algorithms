import sys, heapq
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    # Input
    N,M,X = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a,b,w = map(int,input().split())
        graph[a-1].append((b-1,w))
    
    # Algorithm - Daikstra + BFS
    def daikstra(src):
        heap = [(src,0)]
        dist = [float('inf')]*N
        dist[src] = 0
        while heap:
            node,w = heapq.heappop(heap)
            if w > dist[node]: continue
            
            for neighbor,weight in graph[node]:
                new_w = w + weight
                if new_w < dist[neighbor]:
                    dist[neighbor] = new_w
                    heapq.heappush(heap,(neighbor,new_w))
        return dist

    XtoAny = daikstra(X-1)
    AnytoX = [0]*N
    
    for i in range(N):
        AnytoX[i] = daikstra(i)[X-1]
    
    answer = [0]*N
    for i in range(N):
        answer[i] = XtoAny[i]+AnytoX[i]
    print(max(answer))
    
main()
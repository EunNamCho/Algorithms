import sys, heapq
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    # Input
    V = int(input())
    tree = defaultdict(list)
    for _ in range(V):
        data = deque(map(int,input().split()))
        v = data.popleft()
        while data:
            a = data.popleft()
            if a > 0:
                w = data.popleft()
                tree[v].append((a,w))
        
    # Algorithm - Daikstra
    def daikstra(src):
        dist = [float('inf')]*(V+1)
        dist[0]=-1
        dist[src] = 0
        heap = [(src,0)]
        while heap:
            node,w = heapq.heappop(heap)
            if w > dist[node]: continue
            
            for neighbor, weight in tree[node]:
                new_w = weight + w
                if new_w < dist[neighbor]:
                    dist[neighbor] = new_w
                    heapq.heappush(heap,(neighbor,new_w))
                    
        max_dist, max_node= 0,0
        for node, d in enumerate(dist):
            if max_dist < d:
                max_node = node
                max_dist = d
        return max_node, max_dist
    
    new_node,_ = daikstra(1)
    _,answer = daikstra(new_node)
    
    print(answer)
    
main()
        
import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    N, K = map(int, input().split())
    
    # Algorithm - BFS
    dist = [-1]*100001
    queue = deque([N])
    dist[N] = 0
    ways = [0]*100001
    ways[N] = 1
    
    while queue:
        x = queue.popleft()
        for dx in [1,-1,2]:
            if dx==2:
                nx = x*dx
            else:
                nx = x+dx
            if 0<=nx<=100000:
                if dist[nx]==-1:
                    dist[nx] = dist[x]+1
                    ways[nx] = ways[x]
                    queue.append(nx)
                elif dist[nx]==dist[x]+1:
                    ways[nx] += ways[x]
    print(dist[K])
    print(ways[K])
    # print(ways[:K+1])
                
main()
            
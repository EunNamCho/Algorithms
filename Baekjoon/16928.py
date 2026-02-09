import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int, input().split())
    move = [i for i in range(101)]
    for _ in range(N+M):
        src, dst = map(int, input().split())
        move[src] = dst
        
    # Algorithm - BFS
    queue = deque([1])
    dist = [-1]*101
    dist[1] = 0

    while queue:
        src = queue.popleft()

        for dice in range(1,7):
            next = src+dice
            if next <= 100:
                next = move[next]
                if dist[next]==-1:
                    dist[next] = dist[src]+1
                    queue.append(next)
    # print(dist)
    print(dist[100])
    
main()
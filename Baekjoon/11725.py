import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    # Algorithm - BFS
    queue = deque([1])
    parents = [-1] * (N+1)
    parents[1] = 1
    
    while queue:
        cur_node = queue.popleft()
        
        for neighbor in graph[cur_node]:
            if parents[neighbor]==-1:
                parents[neighbor] = cur_node
                queue.append(neighbor)
    
    for parent in parents[2:]:
        print(parent)
        
main()
    
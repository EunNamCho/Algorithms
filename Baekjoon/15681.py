import sys
from collections import defaultdict, deque
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def main():
    # Input
    N,R,Q = map(int,input().split())
    tree = defaultdict(list)
    queries = []
    for _ in range(N-1):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
    for _ in range(Q):
        queries.append(int(input()))
    
    # Algorithm - BFS
    parents = [-1 for _ in range(N+1)]
    size = [-1 for _ in range(N+1)]
    def bfs(R):
        queue = deque([R])
        visited = [False]*(N+1)
        visited[R] = True
        
        while queue:
            cur = queue.popleft()
            for neighbor in tree[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    parents[neighbor] = cur
                    
    def get_size(node):
        # print(f"Cal {node}: size {size[node]}")
        if size[node]==-1:
            tmp = 0
            for neighbor in tree[node]:
                if parents[neighbor]==node:
                    # print(f"{node}'s child: {neighbor}, size: {size[neighbor]}")
                    tmp += get_size(neighbor)
            size[node] = tmp+1
        # print(f"Cal Done: {node}, size: {size[node]}")
        return size[node]
    
    bfs(R)
    # print(parents)
    get_size(R)
    # print(size)
    for query in queries:
        print(get_size(query))
    
main()
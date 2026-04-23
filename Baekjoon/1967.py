import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N-1):
        a,b,c = map(int,input().split())
        tree[a].append((b,c))
        tree[b].append((a,c))
    
    # Algorithm - DFS
    def dfs(src=0):
        dists = [-1]*(N+1)
        dists[src] = 0
        stack = [(src,0)]
        
        while stack:
            src,dist = stack.pop()
            for neighbor, d in tree[src]:
                if dists[neighbor]==-1:
                    dists[neighbor] = dist+d
                    stack.append((neighbor,dist+d))
        
        max_node, max_dist = 0,0
        
        # 이 부분 그냥 stack 내부에 합칠 수 있음
        for node,dist in enumerate(dists):
            if dist>max_dist:
                max_dist = dist
                max_node = node
        # print(dists)
        return max_node, max_dist
    
    leaf1,tmp = dfs(1)
    # print(leaf1,tmp)
    leaf2,answer = dfs(leaf1)
    # print(leaf1,leaf2,tmp,answer)
    print(answer)

main()
    
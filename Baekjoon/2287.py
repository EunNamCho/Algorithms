import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    nodes = []
    for i in range(N):
        nodes.append((i,tuple(map(int,input().split()))))
    
    # Algorithm - Kruskal
    parents = [i for i in range(N)]
    size = [1 for _ in range(N)]
    MST = 0
    
    def find(x):
        if x!=parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a,b):
        ra,rb = find(a),find(b)
        
        if ra!=rb:
            if size[ra]<size[rb]:
                ra,rb = rb,ra
            parents[rb] = ra
            size[ra] += size[rb]
            return True
        return False
    
    edges = []
    for i in range(3):
        nodes.sort(key=lambda x:x[1][i])
        for j in range(N-1):
            u,v = nodes[j][0], nodes[j+1][0]
            dist = abs(nodes[j][1][i]-nodes[j+1][1][i])
            edges.append((u,v,dist))
    
    edges.sort(key=lambda x: x[2])
    for u,v,w in edges:
        if union(u,v):
            MST += w
    
    print(MST)
    
main()
    
import sys
input = sys.stdin.readline

def main():
    # Input
    V,E = map(int,input().split())
    edges = [tuple(map(int,input().split())) for _ in range(E)] # (u,v,w)
    edges.sort(key=lambda x: x[2])
    
    # Algorithm - Kruskal
    MST = []
    answer = 0
    parents = [i for i in range(V+1)]
    size = [1 for _ in range(V+1)]
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
    
    for u,v,w in edges:
        if union(u,v):
            answer += w
            MST.append((u,v,w))
    
    print(answer-MST[-1][-1])
    
main()
    
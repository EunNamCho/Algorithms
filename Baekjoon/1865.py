import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        # Input
        N,M,W = map(int, input().split())
        edges = []
        for i in range(M+W):
            s,e,t = map(int,input().split())
            if i>=M:
                # print("edges:",s,e,-t)
                edges.append((s,e,-t))
            else:
                edges.append((s,e,t))
                edges.append((e,s,t))
        
        # Algorithm - BellmanFord
        dists = [0]*(N+1) #### 여기가 핵심
        for _ in range(N-1):
            update = False
            
            for u,v,w in edges:
                if dists[u]!=float('inf') and dists[v]>dists[u]+w:
                    dists[v] = dists[u]+w
                    update = True
            
            if not update:
                break
        
        update = False
        for u,v,w in edges:
            if dists[u]!=float('inf') and dists[v]>dists[u]+w:
                update = True
                break
            
        if update:
            print("YES")
        else:
            print("NO")
        # print(dists)

main()
    
import sys
input = sys.stdin.readline

def main():
    # Input
    N,R,Q = map(int,input().split())
    
    # Algorithm - UnionFind
    roots = [i for i in range(N+1)]
    size = [1 for _ in range(N+1)]
    def find(a):
        while True:
            ra = roots[a]
            if a==ra:
                return ra
            a = ra
            
    def union(a,b):
        ra,rb = find(a), find(b)
        if ra!=rb:
            if size[ra] < size[rb]:
                ra,rb = rb,ra
                
            roots[rb] = ra
            size[ra] += size[rb]
            return True
        return False
    
    for k in range(N-1):
        u,v = map(int,input().split())
        union(u,v)
        print(k,roots,size)
    for _ in range(Q):
        print(size[int(input())])
        
main()
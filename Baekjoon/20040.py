import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def main():
    # Input
    N,M = map(int, input().split())
    answer = 0
    
    # Algorithm - Union-Find
    parent = [i for i in range(N)]
    size = [1]*N
    
    # def find(x):
    #     if parent[x]!=x:
    #         parent[x]=find(parent[x])
    #     return parent[x]
    def find(x):
        while x!=parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        pa,pb = find(a), find(b)
        if pa!=pb:
            if size[pa]<size[pb]:
                pa,pb = pb,pa
            parent[pb] = pa
            size[pa]+=size[pb]
            return True
        return False
    
    for i in range(M):
        a,b = map(int,input().split())
        if answer==0 and not union(a,b):
            answer = i+1
    print(answer)

main()
        
import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    lines = [tuple(map(int,input().split())) for _ in range(N)]
    
    # Algorithm - Implementation, UnionFind
    def intersect(l1,l2):
        # y = ax+b
        a1 = (l1[3]-l1[1])/(l1[2]-l1[0])
        b1 = l1[1]-a1*l1[0]
        
        a2 = (l2[3]-l2[1])/(l2[2]-l1[0])
        b2 = l2[1]-a2*l2[0]
        
        
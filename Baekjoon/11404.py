import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    M = int(input())
    dist = [[float("inf")]*N for _ in range(N)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        dist[a-1][b-1] = min(dist[a-1][b-1],c)
    for i in range(N):
        dist[i][i] = 0
    
    # Algorithm - Floyd-Warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                
    for row in dist:
        for col in row:
            if col==float('inf'):
                print(0, end=" ")
            else:
                print(col, end=" ")
        print()
        
main()
    
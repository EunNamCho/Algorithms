import sys
input = sys.stdin.readline

def main():
    # Input
    N, M, R = map(int, input().split())
    items = list(map(int,input().split()))
    matrix = [[float("inf")]*N for _ in range(N)]
    for _ in range(R):
        a,b,l = map(int,input().split())
        matrix[a-1][b-1] = l
        matrix[b-1][a-1] = l
    
    # Algorithm - Floyd-Warshall
    for i in range(N):
        matrix[i][i] = 0
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
                
    answer = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if matrix[i][j] <= M: tmp += items[j]
        answer = max(answer, tmp)
    
    print(answer)
    
main()
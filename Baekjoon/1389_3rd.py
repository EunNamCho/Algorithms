import sys
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int,input().split())
    matrix = [[float('inf')]*N for _ in range(N)]
    for _ in range(M):
        a,b = map(lambda x:int(x)-1,input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    for i in range(N):
        matrix[i][i] = 0
        
    # Algorihtm - Floyd-Warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
    
    # for row in matrix:
    #     print(*row)
    answer,tmp = 0,float('inf')
    for i in range(N):
        if tmp > sum(matrix[i]):
            tmp = sum(matrix[i])
            answer = i+1
    print(answer)
    
main()
import sys
input = sys.stdin.readline

# Input

    
# Algorithm - Floyd-Warshall
def floyd_warshall():
    N, M = map(int, input().split())
    matrix = [[float("inf")]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    for i in range(N):
        matrix[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
                
    min_num, min_vertex = float("inf"), -1
    for i in range(N):
        total = sum(matrix[i])
        if min_num > total:
            min_num = total
            min_vertex = i+1
    # print(matrix)
    print(min_vertex)
    
floyd_warshall()
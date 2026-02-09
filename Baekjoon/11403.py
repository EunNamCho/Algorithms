import sys
input = sys.stdin.readline

# Input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# Algorithm - Floyd-Warshall
for i in range(N):
    for j in range(N):
        if matrix[i][j]==0:
            matrix[i][j] = float("inf")
        elif i==j:
            matrix[i][j] = 1
            
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])

for row in range(N):
    for col in range(N):
        if matrix[row][col]==float("inf") or matrix[row][col]==0:
            print(0, end=" ")
        elif matrix[row][col]>0:
            print(1, end=" ")
    print()

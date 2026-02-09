import sys
from collections import deque
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(input().rstrip())
for row in range(N):
    for col in range(M):
        if matrix[row][col]=="I":
            start = [row,col]

# Algorithm - BFS
def bfs(r,c):
    answer = 0
    queue = deque([[r,c]])
    visited = [[False]*M for _ in range(N)]
    visited[r][c] = True
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                if matrix[nr][nc]=="P" :
                    answer += 1
                    visited[nr][nc] = True
                    queue.append([nr,nc])
                elif matrix[nr][nc]=="O":
                    visited[nr][nc] = True
                    queue.append([nr,nc])
    return answer

answer = bfs(*start)
if answer>0:
    print(answer)
else:
    print("TT")
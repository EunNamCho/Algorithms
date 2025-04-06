# 15분
import sys
from collections import deque

# input
M,N = map(int, sys.stdin.readline().strip().split())
matrix = []
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
queue = deque([])
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().strip().split())))
for y, row in enumerate(matrix):
    for x, _ in enumerate(row):
        if matrix[y][x]==1:
            queue.append((y,x))

# algorithm - BFS
def bfs():
    answer = -1
    while queue:
        src_y, src_x = queue.popleft()
        for dy, dx in dirs:
            new_y, new_x = src_y+dy, src_x+dx
            if (0<=new_y<N) and (0<=new_x<M) and matrix[new_y][new_x]==0:
                matrix[new_y][new_x] = matrix[src_y][src_x] + 1
                queue.append((new_y,new_x))
    for row in matrix:
        for col in row:
            if col==0:
                return 0
            else:
                answer = max(answer, col)
    return answer
    
# output
print(bfs()-1)
import sys
from collections import deque

# input
N, M = map(int, sys.stdin.readline().strip().split())
dirs = [(1,0),(-1,0),(0,1),(0,-1)] # dx,dy
matrix = []
dst = None
cost = [[0]*M for _ in range(N)]
for y in range(N):
    matrix.append(list(map(int,sys.stdin.readline().strip().split())))
    for x in range(M):
        if matrix[y][x]==2:
            dst = (x, y)
cost[dst[1]][dst[0]] = 0

# input check
# for row in matrix:
#     print(row)
# print(dst)

# algorithm - BFS
queue = deque([dst])
while queue:
    x, y = queue.popleft()
    for dx, dy in dirs:
        new_x, new_y = x+dx, y+dy
        if (0<=new_x<M) and (0<=new_y<N):
            if matrix[new_y][new_x]==1:
                matrix[new_y][new_x] = 0
                cost[new_y][new_x] = cost[y][x] + 1
                queue.append((new_x,new_y))
for y,row in enumerate(matrix):
    for x,_ in enumerate(row):
        if matrix[y][x]==1:
            cost[y][x]=-1

for y, row in enumerate(cost):
    for x, _ in enumerate(row):
        print(cost[y][x], end=" ")
    print()
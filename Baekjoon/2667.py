# 15분 소요

import sys
sys.setrecursionlimit(100000000)

# input
N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().strip())))
answer = []
dirs = [(1,0),(-1,0),(0,1),(0,-1)] # dx, dy

 # input check
# for row in matrix:
#     print(row)
# print(matrix[1][1])

# algorithm - DFS
def iter_dfs():
    for y, row in enumerate(matrix):
        for x, _ in enumerate(row):
            if matrix[y][x]==1:
                answer.append(1)
                dfs(x, y)

def dfs(x, y):
    matrix[y][x] = 0
    for dx, dy in dirs:
        new_x, new_y = x+dx, y+dy
        if (0<=new_x<N) and (0<=new_y<N):
            if matrix[new_y][new_x]==1:
                answer[-1] += 1
                dfs(new_x,new_y)

iter_dfs()
print(len(answer))
for n in sorted(answer):
    print(n)
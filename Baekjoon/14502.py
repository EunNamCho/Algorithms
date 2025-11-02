import sys
from copy import deepcopy

# input 
N,M = map(int, sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
safe_zones = []
viruses = []
answer = 0
for row,_ in enumerate(matrix):
    for col,_ in enumerate(matrix[row]):
        if matrix[row][col]==0:
            safe_zones.append((row,col))
        if matrix[row][col]==2:
            viruses.append((row,col))
            
# algorithm - BackTracking
def dfs(matrix):
    global viruses
    stack = deepcopy(viruses)
    while stack:
        vy,vx = stack.pop()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny = vx+dx, vy+dy
            if 0<=ny<N and 0<=nx<M and matrix[ny][nx]==0:
                matrix[ny][nx] = 2
                stack.append((ny,nx))
        
def count(matrix):
    safe = 0
    for row in matrix:
        for col in row:
            if col==0:
                safe+=1
    return safe
        
def back(polls,matrix,start):
    global safe_zones,answer
    if len(polls)==3:
        tmp = [row[:] for row in matrix]
        dfs(tmp)
        # print("="*30)
        # print(polls)
        # for row in tmp:
        #     for col in row:
        #         print(col, end=" ")
        #     print()
        answer = max(answer, count(tmp))
        # print(answer)
        return
    
    for idx,safe_zone in enumerate(safe_zones[start:]):
        polls.append(safe_zone)
        matrix[safe_zone[0]][safe_zone[1]]=1
        back(polls,matrix,start+idx+1)
        matrix[safe_zone[0]][safe_zone[1]]=0
        polls.pop()

back([],matrix,0)
print(answer)
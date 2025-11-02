import sys
from collections import deque

# input
N,M = map(int, sys.stdin.readline().split())
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
matrix = []
answer = [float("inf")]
for _ in range(N):
    row = list(sys.stdin.readline().strip())
    matrix.append(row)
    
R,B = (0,0), (0,0)
visited = set()
queue = deque()
for i,row in enumerate(matrix):
    for j,col in enumerate(row):
        if matrix[i][j]=="R":
            R = (i,j)
        elif matrix[i][j]=="B":
            B = (i,j)
# matrix[R[0]][R[1]] = 0
matrix[R[0]][R[1]]="."
matrix[B[0]][B[1]]="."
# input check
# for row in matrix:
#     print(row)

# Algorithm - Brute Force
def roll(x,y,dx,dy):
    dist = 0
    while True:
        nx, ny = x+dx, y+dy
        if matrix[nx][ny]=="#":
            return x,y,dist,False
        elif matrix[nx][ny]=="O":
            return x,y,dist,True
        x, y = nx, ny
        dist+=1
        
def bfs():
    queue.append((*R,*B,0))
    visited.add((*R,*B))
    while queue:
        r_xpos, r_ypos, b_xpos, b_ypos, depth = queue.popleft()

        if depth >= 10:
            continue
        for dir in dirs:
            dx, dy = dir
            new_r_xpos, new_r_ypos, r_dist, r_hole = roll(r_xpos, r_ypos, dx, dy)
            new_b_xpos, new_b_ypos, b_dist, b_hole = roll(b_xpos, b_ypos, dx, dy)
            
            # print(dx,dy)
            # print(new_r_xpos, new_r_ypos, r_dist, r_hole)
            # print(new_b_xpos, new_b_ypos, b_dist, b_hole)
            
            if b_hole:
                continue
            elif r_hole:
                print(depth+1)
                sys.exit(0)
            
            if new_r_xpos==new_b_xpos and new_r_ypos==new_b_ypos:
                if r_dist < b_dist:
                    new_b_xpos, new_b_ypos = new_b_xpos-dx, new_b_ypos-dy
                else:
                    new_r_xpos, new_r_ypos = new_r_xpos-dx, new_r_ypos-dy
            
            if (new_r_xpos, new_r_ypos,new_b_xpos,new_b_ypos) not in visited:
                # input check
                # for i in range(N):
                #     for j in range(M):
                #         if i==new_r_xpos and j==new_r_ypos:
                #             print("R", end="")
                #         elif i==new_b_xpos and j==new_b_ypos:
                #             print("B", end="")
                #         else:
                #             print(matrix[i][j],end="")
                #     print()
                # print()
                queue.append((new_r_xpos, new_r_ypos,new_b_xpos,new_b_ypos, depth+1))
                visited.add((new_r_xpos, new_r_ypos,new_b_xpos,new_b_ypos))
            # print(queue)
    print(-1)
    sys.exit(0)
    
bfs()
            
                    
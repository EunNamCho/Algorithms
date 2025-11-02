import sys

# input
N,M = map(int, sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
UP, DOWN, LEFT, RIGHT = (-1,0), (1,0), (0,-1), (0,1)
cctvs = []
answer = float('inf')
dirs = {
    1:[[UP],[RIGHT],[DOWN],[LEFT]],
    2:[[UP,DOWN],[LEFT,RIGHT]],
    3:[[UP,RIGHT],[RIGHT,DOWN],[DOWN,LEFT],[LEFT,UP]],
    4:[[UP,RIGHT,DOWN],[RIGHT,DOWN,LEFT],[DOWN,LEFT,UP],[LEFT,UP,RIGHT]],
    5:[[UP,RIGHT,DOWN,LEFT]]
}
for i,row in enumerate(matrix):
    for j,col in enumerate(row):
        if 1<=col<=5:
            cctvs.append((i,j))
            
# algorithm - Backtracking
def watch(r,c,direction):
    global matrix
    watched = []
    for dr,dc in direction:
        nr,nc = r,c
        while True:
            nr,nc = dr+nr,dc+nc
            if 0<=nr<N and 0<=nc<M:
                if matrix[nr][nc]<=0:
                    matrix[nr][nc]-=1
                    watched.append((nr,nc))
                elif matrix[nr][nc]==6:
                    break
            else:
                break
    return watched

def undo(watched):
    global matrix
    # print(watched)
    for r,c in watched:
        matrix[r][c]+=1

def check():
    global matrix
    unwatched = 0
    for row in matrix:
        for col in row:
            if col==0:
                unwatched+=1
    return unwatched

def back(idx):
    global answer,cctvs
    if idx==len(cctvs):
        answer = min(answer,check())
        # print("="*30)
        # for row in matrix:
        #     for col in row:
        #         print(col,end=" ")
        #     print()
        return
        
    r,c = cctvs[idx]
    t = matrix[r][c]
    for direction in dirs[t]:
        watched = watch(r,c,direction)
        back(idx+1)
        undo(watched)

back(0)
print(answer)
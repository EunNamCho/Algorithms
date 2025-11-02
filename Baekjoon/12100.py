import sys
from collections import deque, defaultdict
from copy import deepcopy
sys.setrecursionlimit(1000000)

# input
N = int(sys.stdin.readline())
answer = -1
matrix = []
for i in range(N):
    matrix.append(list(map(int,sys.stdin.readline().strip().split())))
    for j in range(N):
        answer = max(answer,matrix[i][j])
    
# input-check
# for i in range(N):
#     for j in range(N):
#         print(matrix[i][j], end=" ")
#     print()
# print()
# print(answer)

# Algorithm - BackTracking
def move_left(bd):
    cp = deepcopy(bd)
    for i in range(N):
        for j in range(1,N):
            for k in range(0,j):
                if cp[i][j-1+k]==cp[i][j+k]:
                    cp[i][j-1+k]*=2
                    cp[i][j+k]=0
                    break
                elif cp[i][j-1+k]==0:
                    cp[i][j-1+k]=cp[i][j+k]
                    cp[i][j+k]=0
                else:
                    break
    return cp

def move_right(bd):
    cp = deepcopy(bd)
    for i in range(N):
        for j in range(N-2,-1,-1):
            for k in range(0,N-j-1):
                if cp[i][j+k]==cp[i][j+1+k]:
                    cp[i][j+1+k]*=2
                    cp[i][j+k]=0
                    break
                elif cp[i][j+1+k]==0:
                    cp[i][j+1+k]=cp[i][j+k]
                    cp[i][j]=0
                else:
                    break
    return cp

def move_up(bd):
    cp = deepcopy(bd)
    for i in range(1,N):
        for j in range(N):
            for k in range(0,j):
                if cp[i+k][j]==cp[i-1+k][j]:
                    cp[i-1+k][j]*=2
                    cp[i+k][j]=0
                    break
                elif cp[i-1+k][j]==0:
                    cp[i-1+k][j]=cp[i+k][j]
                    cp[i+k][j]=0
                else:
                    break
    return cp

def move_down(bd):
    cp = deepcopy(bd)
    for i in range(N-2,-1,-1):
        for j in range(N):
            for k in range(0,N-j-1):
                if cp[i+k][j]==cp[i+1+k][j]:
                    cp[i+1+k][j]*=2
                    cp[i+k][j]=0
                elif cp[i+1+k][j]==0:
                    cp[i+1+k][j]=cp[i+k][j]
                    cp[i+k][j]=0
    return cp

def find_max(bd):
    m = 0
    for i in range(N):
        for j in range(N):
            m = max(m,bd[i][j])
    return m

def back(move,bd):
    global answer
    if move==5:
        for i in range(N):
            for j in range(N):
                print(bd[i][j], end=" ")
            print()
        print()
        answer = max(answer,find_max(bd))
        return
    
    for mover in [move_down,move_left,move_right,move_up]:
        new_bd = mover(bd)
        # import pdb; pdb.set_trace()
        
        # for i in range(N):
        #     for j in range(N):
        #         print(bd[i][j], end=" ")
        #     print()
        # print()
        if new_bd==bd:
            continue
        back(move+1,new_bd)
        
back(0,matrix)

print(answer)
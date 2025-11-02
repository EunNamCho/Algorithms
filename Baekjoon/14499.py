import sys

# input
N,M,X,Y,_ = map(int, sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
Ks = list(map(int,sys.stdin.readline().split())) 
dirs = [(0,1),(0,-1),(-1,0),(1,0)] # E:0, W:1, N:2, S:3
dice = [0]*6 # T, B, E, W, S, N

# algorithm - Implementation
def roll(dice, direction):
    if direction==0:
        # T=>E, B=>W, E=>B, W=>T, S=>S, N=>N
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[2],dice[0],dice[1],dice[4],dice[5]
    elif direction==1:
        # T=>W, B=>E, E=>T, W=>B, S=>S, N=>N
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[3],dice[1],dice[0],dice[4],dice[5]
    elif direction==3:
        # T=>S, B=>N, E=>E, W=>W, S=>B, N=>T
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[5],dice[4],dice[2],dice[3],dice[0],dice[1]
    else:
        # T=>N, B=>S, E=>E, W=>W, S=>T, N=>B
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[5],dice[2],dice[3],dice[1],dice[0]
    return dice

def Imple():
    global N,M,X,Y,matrix,Ks,dirs,dice
    for k in Ks:
        dr, dc = dirs[k-1]
        nr, nc = X+dr, Y+dc
        if 0<=nr<N and 0<=nc<M:
            X,Y=nr,nc
            dice = roll(dice,k-1)
            if matrix[X][Y]==0:
                matrix[X][Y] = dice[1]
            else:
                dice[1] = matrix[X][Y]
                matrix[X][Y] = 0
            print(dice[0])
            # print(X,Y,dice)
Imple()
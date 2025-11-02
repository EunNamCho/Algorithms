import sys

# input
N, M = map(int, sys.stdin.readline().split())
r,c,d = map(int, sys.stdin.readline().split()) 
dirs = [(-1,0),(0,1),(1,0),(0,-1)] # d:0=>N, d:1=>E, d:2=>S, d:3=>W
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = 0

# input check
# for row in matrix:
#     for col in row:
#         print(col,end=" ")
#     print()
    
# algorithm - Implementation
def Imple():
    global r,c,d,matrix,answer
    while True:
        find=False
        if matrix[r][c]==0:
            matrix[r][c]=2
            answer+=1
        # print('='*30)
        # print(r,c,d)
        # for row in matrix:
        #     for col in row:
        #         print(col, end=" ")
        #     print()
        for i in range(1,5):
            nd = (d-i)%4
            dr,dc=dirs[nd]
            # print(nd)
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M and matrix[nr][nc]==0:
                r,c,d = nr,nc,nd
                find=True
                break
        if find:
            continue
        dr,dc = dirs[d]
        nr,nc=r-dr,c-dc
        if 0<=nr<N and 0<=nc<M:
            if matrix[nr][nc]==1:
                return answer
            else:
                r,c,d = nr,nc,d

print(Imple())
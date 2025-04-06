# is_valid로 검사하니까, 시간초과. 캐싱쓰니까 통과.
# GPT가 알려줌.
# 해 하나만 찾으려면, sys.exit(0)으로 강제종료.
import sys
sys.setrecursionlimit(10000000)

# input
N = 9
matrix = []
zeros = []
rows = [[False]*10 for _ in range(N)]
cols = [[False]*10 for _ in range(N)]
segms = [[False]*10 for _ in range(N)]
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for y, row in enumerate(matrix):
    for x, _ in enumerate(row):
        if matrix[y][x]==0:
            zeros.append((y,x))
        else:
            rows[y][matrix[y][x]]=True
            cols[x][matrix[y][x]]=True
            segms[x//3+(y//3)*3][matrix[y][x]]=True

# input check
# print(zeros)

# algorithm - Backtracking
# def is_valid(y, x, number):
#     tgt = number

#     # 행
#     for nx in range(N):
#         if matrix[y][nx]==tgt:
#             return False
        
#     # 열
#     for ny in range(N):
#         if matrix[ny][x]==tgt:
#             return False
    
#     # 세그먼트
#     sy, sx = y//3, x//3
#     for ky in range(3):
#         for kx in range(3):
#             if matrix[ky+sy*3][kx+sx*3]==tgt:
#                 return False
            
#     return True
        
def back(idx):
    # termination
    if idx==len(zeros):
        for row in matrix:
            print(" ".join(map(str, row)))
        sys.exit(0)

    y, x = zeros[idx]
    for number in range(1,N+1):
        if not rows[y][number] and not cols[x][number] and not segms[x//3+(y//3)*3][number]:
            matrix[y][x] = number
            rows[y][number] = cols[x][number] = segms[x//3+(y//3)*3][number] = True
            back(idx+1)
            matrix[y][x] = 0
            rows[y][number] = cols[x][number] = segms[x//3+(y//3)*3][number] = False

back(0)

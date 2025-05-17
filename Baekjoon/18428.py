import sys
from itertools import combinations
sys.setrecursionlimit(100000)

# input
N = int(sys.stdin.readline())
matrix = []
teachers, emptys = [], []
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(N):
    matrix.append(sys.stdin.readline().split())
for row, _ in enumerate(matrix):
    for col, _ in enumerate(matrix[row]):
        if matrix[row][col]=="T":
            teachers.append((row,col))
        elif matrix[row][col]=="X":
            emptys.append((row,col))
C = combinations(emptys,3)

# input check
# for i,items in enumerate(C):
#     if i==2:break
#     print(items)
# print(teachers)

# algorithm - combinations
def detect():
    for teacher in teachers:
        row, col = teacher
        for dir in dirs:
            ny, nx = dir
            new_row, new_col = row, col
            while True:
                new_row, new_col = ny+new_row, nx+new_col
                if 0<=new_row<N and 0<=new_col<N:
                    if matrix[new_row][new_col]=="S":
                        return True
                    elif matrix[new_row][new_col]=="O":
                        break
                else:
                    break
    return False

for i, items in enumerate(C):
    for item in items:
        row,col = item
        matrix[row][col]="O"
    if not detect():
        print("YES")
        sys.exit()
    for item in items:
        row,col = item
        matrix[row][col]="X"
print("NO")
        
    
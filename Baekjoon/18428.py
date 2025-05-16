import sys
sys.setrecursionlimit(100000)

# input
N = int(sys.stdin.readline())
matrix = []
det_row, det_col = [False]*N, [False]*N
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

for row, _ in enumerate(matrix):
    for col, _ in enumerate(row):
        if matrix[row][col]=="T":
            det_row[row] = True
            det_col[col] = True

# algorithm - BackTracking
def back(row, num):
    global answer
    if num==4:
        detect = False
        for i in range(N):
            if det_row[i]==True or det_col[i]==True:
                detect = True
                break
        if not detect:
            print("YES")
            sys.exit()
        return
    for i in range(N):
        
    
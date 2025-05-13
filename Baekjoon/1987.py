import sys
sys.setrecursionlimit(100000)

# input
R,C = map(int,sys.stdin.readline().split())
matrix = []
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
answer = [0]
for _ in range(R):
    matrix.append(sys.stdin.readline().strip())
visited = [0] * 26

# algorithm - DFS
def dfs(row,col):
    visited[ord(matrix[row][col])-65] = 1
    answer[0] = max(answer[0],sum(visited))
    for dir in dirs:
        dx,dy = dir
        new_row, new_col = row+dy, col+dx
        if 0<=new_row<R and 0<=new_col<C and not visited[ord(matrix[new_row][new_col])-65]:
            dfs(new_row,new_col)
    visited[ord(matrix[row][col])-65] = 0
    

dfs(0,0)
print(answer[0])
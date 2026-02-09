import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    matrix = [input().rstrip() for _ in range(N)]

    # Algorithm - BFS
    def BFS(matrix, mode):
        queue = deque()
        visited = [[False]*N for _ in range(N)]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        component = 0

        for row in range(N):
            for col in range(N):
                if not visited[row][col]:
                    queue.append((row,col))
                    visited[row][col] = True
                    component += 1
            
                while queue:
                    r, c = queue.popleft()
                    if mode=="RG":
                        if matrix[r][c] in ["R", "G"]:
                            color = ["R", "G"]
                        else:
                            color = ["B"]
                    elif mode=="RGB":
                        color = [matrix[r][c]]

                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<N and 0<=nc<N and matrix[nr][nc] in color and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr,nc))
        return component
    
    print(BFS(matrix,"RGB"), BFS(matrix,"RG"))
    
main()
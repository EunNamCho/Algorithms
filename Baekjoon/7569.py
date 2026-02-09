import sys
from collections import deque
input = sys.stdin.readline

# Input
def main():
    M, N, H = map(int, input().split())
    matrix = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
        
    # Algorithm - BFS
    non_ripe = 0
    days = 1
    queue = deque()
    dirs = [[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
    for channel in range(H):
        for row in range(N):
            for col in range(M):
                if matrix[channel][row][col]==1:
                    queue.append((channel,row,col))
                elif matrix[channel][row][col]==0:
                    non_ripe += 1

    # print(matrix)
    # print(visited)
    if non_ripe>0:
        while queue:
            ch, r, c = queue.popleft()
            for dch, dr, dc in dirs:
                nch, nr, nc = ch+dch, r+dr, c+dc
                if 0<=nch<H and 0<=nr<N and 0<=nc<M and matrix[nch][nr][nc]==0:
                    matrix[nch][nr][nc] = matrix[ch][r][c]+1
                    days = max(days, matrix[nch][nr][nc])
                    non_ripe -= 1
                    queue.append((nch,nr,nc))
    if non_ripe>0:
        print(-1)
    else:
        print(days-1)  
        
main()
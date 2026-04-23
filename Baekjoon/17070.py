import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    # Algorithm - BFS
    def find_shape(head, tail):
        r,c = tail[0] - head[0], tail[1] - head[1]
        if r==0:
            return 0
        elif c==0:
            return 2
        else:
            return 1
        
    def avail_rotate(tail):
        r,c = tail
        for r,c in [(r,c+1),(r+1,c+1),(r+1,c)]:
            if 0<=r<N and 0<=c<N and matrix[r][c]!=1:
                pass
            else:
                return 0
        return 3
        
    dist = [[-1]*N for _ in range(N)]
    path = [[0]*N for _ in range(N)]
    queue = deque([((0,0),(0,1))]) # head, tail
    dirs = [
        # beelines    
        [(0,1)],
        [(1,0),(0,1)],
        [(1,0)],
        # rotate
        [(0,1),(1,1)],
        [(1,0),(1,1),(0,1)],
        [(1,0),(1,1)]
    ]
    dist[0][0] = 0
    dist[0][1] = 0
    path[0][0] = 1
    path[0][1] = 1
    
    while queue:
        head, tail = queue.popleft()
        dir_idx = find_shape(head,tail) + avail_rotate(tail)
        
        for dr,dc in dirs[dir_idx]:
            n_head, n_tail = (tail[0],tail[1]), (tail[0]+dr,tail[1]+dc)
            if 0<=n_tail[0]<N and 0<=n_tail[1]<N and matrix[n_tail[0]][n_tail[1]]!=1:
                if dist[n_tail[0]][n_tail[1]]==-1:
                    dist[n_tail[0]][n_tail[1]] = dist[n_head[0]][n_head[1]]+1
                    path[n_tail[0]][n_tail[1]] = path[n_head[0]][n_head[1]]
                    queue.append((n_head,n_tail))
                elif  dist[n_head[0]][n_head[1]]+1==dist[n_tail[0]][n_tail[1]]:
                    path[n_tail[0]][n_tail[1]] += path[n_head[0]][n_head[1]]
                    queue.append((n_head,n_tail))
                    
        print(head,tail)
        print("path=============")
        for row in path:
            for col in row:
                print(col, end=" ")
            print()
        print("dist=============")
        for row in dist:
            for col in row:
                print(col, end=" ")
            print()
        print()

    print(path[N-1][N-1])
    
import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # 목적지가 벽이면 시작도 하기 전에 0
    if board[N-1][N-1] == 1:
        print(0)
        return

    # 큐 데이터: (행, 열, 방향)
    # 방향: 0(가로), 1(세로), 2(대각선)
    queue = deque([(0, 1, 0)])
    count = 0
    
    while queue:
        r, c, d = queue.popleft()
        
        # 목적지 도달 시 카운트 증가
        if r == N-1 and c == N-1:
            count += 1
            continue
            
        # 1. 가로로 이동 (현재 가로(0)거나 대각선(2)일 때만 가능)
        if d == 0 or d == 2:
            if c + 1 < N and board[r][c+1] == 0:
                queue.append((r, c+1, 0))
                
        # 2. 세로로 이동 (현재 세로(1)거나 대각선(2)일 때만 가능)
        if d == 1 or d == 2:
            if r + 1 < N and board[r+1][c] == 0:
                queue.append((r+1, c, 1))
                
        # 3. 대각선으로 이동 (모든 방향에서 가능)
        if r + 1 < N and c + 1 < N:
            if board[r+1][c] == 0 and board[r][c+1] == 0 and board[r+1][c+1] == 0:
                queue.append((r+1, c+1, 2))
                
    print(count)

solve()
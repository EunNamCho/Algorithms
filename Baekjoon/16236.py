import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    shark_size, shark = 2, (0,0)
    eaten_fishes = 0
    answer = 0
    for row in range(N):
        for col in range(N):
            if board[row][col]==9:
                shark = (row,col)
                board[row][col] = 0
                break
    
    # Algorithm - Implementation
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    def find_fishes(shark_size,shark):
        visited = [[False]*N for _ in range(N)]
        visited[shark[0]][shark[1]] = True
        shortest_dist = 0
        fishes = []
        queue = deque([(shark,0)])
        
        while queue:
            (r,c),dist = queue.popleft()
            # print(r,c,fishes,shortest_dist)
            if shortest_dist!=0 and dist>shortest_dist: break
            
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<N and 0<=nc<N and board[nr][nc]<=shark_size and not visited[nr][nc]:
                    if board[nr][nc]!=0 and board[nr][nc]<shark_size and shortest_dist==0:
                        shortest_dist = dist+1
                        fishes.append((nr,nc))
                    elif board[nr][nc]!=0 and board[nr][nc]<shark_size and shortest_dist==(dist+1):
                        fishes.append((nr,nc))
                    visited[nr][nc] = True
                    queue.append(((nr,nc),dist+1))
        
        return shortest_dist, fishes
    
    def eat_fish(fishes):
        min_r = []
        for r,c in fishes:
            if not min_r:
                min_r.append((r,c))
            else:
                if min_r[-1][0]>r:
                    min_r = [(r,c)]
                elif min_r[-1][0]==r:
                    min_r.append((r,c))
        
        if len(min_r)>1:
            min_c = []
            for r,c in min_r:
                if not min_c:
                    min_c.append((r,c))
                else:
                    if min_c[-1][1]>c:
                        min_c = [(r,c)]
                    elif min_r[-1][1]==c:
                        min_r.append((r,c))
            return min_c[0]
        return min_r[0]
            
    while True:
        shortest_dist, fishes = find_fishes(shark_size,shark)
        if shortest_dist==0:
            print(answer)
            break
        else:
            shark = eat_fish(fishes)
            board[shark[0]][shark[1]] = 0
            eaten_fishes += 1
            answer += shortest_dist
            if eaten_fishes==shark_size:
                shark_size += 1
                eaten_fishes = 0
        # print(shortest_dist,shark,eaten_fishes,shark_size)
        # for row in board:
        #     print(*row)
                
main()
    
import sys
from collections import deque
input = sys.stdin.readline
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    # Input
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cheese = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c]==1: cheese.append((r,c))
    
    # Algorithm - BFS & Implementation
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    def bfs(hour):
        n_hour = hour+2
        matrix[0][0] = n_hour
        queue = deque([(0,0)])
        
        while queue:
            r,c = queue.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M and matrix[nr][nc]!=1 and matrix[nr][nc]!=n_hour:
                    queue.append((nr,nc))
                    matrix[nr][nc] = n_hour
                    
    def melt():
        remain_cheese = []
        for r,c in cheese:
            cnt = 0
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M and matrix[nr][nc]!=1 and matrix[nr][nc]!=0:
                    cnt+=1
            if cnt>=2:
                matrix[r][c] = 0
            else:
                remain_cheese.append((r,c))
        return remain_cheese
    
    time = 0
    while cheese:
        bfs(time)
        cheese = melt()
        time += 1
    print(time)
    
main()

#####################
import sys
from collections import deque
input = sys.stdin.readline
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    # Input
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cheese = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c]==1: cheese.append((r,c))
    
    # Algorithm - BFS & Implementation
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    def bfs(src):
        matrix[src[0]][src[1]] = 2
        queue = deque([src])
        
        while queue:
            r,c = queue.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M and matrix[nr][nc]==0:
                    queue.append((nr,nc))
                    matrix[nr][nc] = 2
                    
    def melt():
        remain_cheese = []
        melt_cheese = []
        for r,c in cheese:
            cnt = 0
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M and matrix[nr][nc]!=1 and matrix[nr][nc]!=0:
                    cnt+=1
            if cnt>=2:
                melt_cheese.append((r,c))
                matrix[r][c] = 0
            else:
                remain_cheese.append((r,c))
        return melt_cheese, remain_cheese
    
    time = 0
    melt_cheese = []
    while cheese:
        if not melt_cheese:
            srcs = [(0,0)]
        else:
            srcs = melt_cheese
        for src in srcs:
            bfs(src)
        melt_cheese, cheese = melt()
        time += 1
    print(time)
    
main()
from collections import deque

n,m = map(int, input().split())

matrix = []
visited = []

for _ in range(n):
    matrix.append(list(map(int, input())))
    visited.append([0]*m)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for dy, dx in dirs:
            if (0<=y+dy<n) and (0<=x+dx<m):
                if matrix[y+dy][x+dx]==1:
                    matrix[y+dy][x+dx]=0
                    visited[y+dy][x+dx] = visited[y][x] + 1
                    queue.append((x+dx,y+dy))
    return visited[n-1][m-1] + 1

print(bfs())
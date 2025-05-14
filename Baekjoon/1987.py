import sys

r, c = map(int, sys.stdin.readline().split())
graph = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))

def dfs(sx,sy):
    q = set()
    q.add((sx,sx,graph[sx][sy]))
    squares = 0

    while q:
        x, y, now_visited = q.pop()

        squares = max(squares, len(now_visited))
        if squares == 26:
            return 26
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] not in now_visited:
                q.add((nx, ny, now_visited + graph[nx][ny]))
    return squares
print(dfs(0,0))


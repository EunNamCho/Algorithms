def solution(maps):
    from collections import deque
    def bfs(start, goal):
        n, m = len(maps), len(maps[0])
        queue = deque([start])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while queue:
            x, y, dist = queue.popleft()
            if (x,y) == goal:
                return dist
            for dir in directions:
                nx, ny = x + dir[0], y + dir[1]
                if n > nx >= 0 and m > ny >= 0 and maps[nx][ny]==1:
                    maps[nx][ny] = 0
                    queue.append((nx,ny,dist+1))
        return -1
    start = (0,0,1)
    goal = (len(maps)-1, len(maps[0])-1)
    return bfs(start, goal)



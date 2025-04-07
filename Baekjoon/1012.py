import sys
sys.setrecursionlimit(1000000)

# input
T = int(sys.stdin.readline().strip())
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

# algorithm - DFS or BFS
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    answer = 0

    # matrix creation
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        matrix[y][x] = 1

    def iter_dfs(answer):
        for y, row in enumerate(matrix):
            for x, _ in enumerate(row):
                if matrix[y][x]==1:
                    dfs(x, y)
                    answer += 1    
        print(answer)

    def dfs(x, y):
        matrix[y][x] = 0
        for dy, dx in dirs:
            new_y, new_x = y+dy, x+dx
            if (0<=new_y<N) and (0<=new_x<M):
                if matrix[new_y][new_x]==1:
                    dfs(new_x, new_y)
    
    # DFS
    iter_dfs(answer)
    
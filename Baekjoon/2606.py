import sys

# input
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
network = [[0]*N for _ in range(N)]
visited = [False]*N
answer = [0]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().strip().split())
    network[src-1][dst-1] = 1
    network[dst-1][src-1] = 1

# input check
# for row in network:
#     print(row)

# algorithm - DFS
def iter_dfs():
    for vertex, _ in enumerate(network[0]):
        if network[0][vertex]==1 and not visited[vertex]:
            visited[0] = True
            dfs(0, vertex)

def dfs(src, dst):
    answer[0] += 1
    visited[dst] = True
    for vertex, _ in enumerate(network[dst]):
        if network[dst][vertex]==1 and not visited[vertex]:
            dfs(dst, vertex)

iter_dfs()
print(answer[0])
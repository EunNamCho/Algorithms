import sys

# input
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = []
for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    edges.append((c,a,b)) # (weight, src, dst)
parents = [i for i in range(N+1)]
size = [1] * (N+1)
answer = 0

# Algorightm - Kruskal
def find(u):
    if u!=parents[u]:
        parents[u] = find(parents[u])
    # print(parents)
    return parents[u]
        
edges.sort()
cnt = 0
for weight, a, b in edges:
    root_a, root_b = find(a), find(b)
    if root_a!=root_b:
        if size[root_a] < size[root_b]:
            parents[root_a] = root_b
            size[root_b] += size[root_a]
        else:
            parents[root_b] = root_a
            size[root_a] += size[root_b]

        answer += weight
        cnt += 1
    if cnt==N-1:
        break
if cnt!=N-1:
    print(-1)
else:
    print(answer)
# print(parents)
    
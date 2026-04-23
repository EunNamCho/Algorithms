import sys
input = sys.stdin.readline

def main():
    # Input
    N,M = map(int, input().split())
    dists = [[float('inf')]*N for _ in range(N)]
    answer = float('inf')
    for _ in range(M):
        a,b = map(lambda x: int(x)-1, input().split())
        dists[a][b] = 1
        dists[b][a] = 1
    
    # Algorithm - Floyd-Warshall
    for i in range(N):
        dists[i][i] = 0
            

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dists[i][j] = min(dists[i][j], dists[i][k]+dists[k][j])
    
    min_num, min_vertex = float("inf"), -1
    for i in range(N):
        total = sum(dists[i])
        if min_num > total:
            min_num = total
            min_vertex = i+1
            
    print(min_vertex)
    
main()


def solution(p):
    answer = 0
    p.sort(reverse=True)
    stack = p[0]
    
    for i in range(1,len(p)):
        if stack[-1]>p[i]:
            stack.pop()
            stack.append(p[i])
            answer+=1
        else:
            stack.append(p[i])
    return answer
    
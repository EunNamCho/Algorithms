import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    N, K = map(int, input().split())
    
    # Algorithm - BFS
    dist = [-1]*(100_001)
    queue = deque([N])
    dist[N] = 0

    while queue:
        cur_pos = queue.popleft()
        if cur_pos==K:
            print(dist[K])
            return
        for ops_idx, neighbor in enumerate([cur_pos-1, cur_pos+1, 2*cur_pos]):
            if 0<=neighbor<=100_000 and dist[neighbor]==-1:
                if ops_idx==2:
                    queue.appendleft(neighbor)
                    dist[neighbor] = dist[cur_pos]
                else:
                    queue.append(neighbor)
                    dist[neighbor] = dist[cur_pos]+1
    
main()


import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    
    # 최대 범위 100,000까지 방문 여부 및 소요 시간 저장
    # -1로 초기화하여 방문하지 않은 상태를 표시
    dist = [-1] * 100001
    
    queue = deque([n])
    dist[n] = 0
    
    while queue:
        curr = queue.popleft()
        
        # 동생을 찾으면 종료
        if curr == k:
            print(dist[curr])
            return
        
        # 1. 순간이동 (0초 소요) - 가장 높은 우선순위
        # 현재 위치의 2배로 이동, 범위 내에 있고 아직 방문 안 했거나 더 짧은 경로라면
        nxt_teleport = curr * 2
        if 0 <= nxt_teleport <= 100000 and dist[nxt_teleport] == -1:
            dist[nxt_teleport] = dist[curr]
            queue.appendleft(nxt_teleport) # 가중치가 0이므로 앞쪽에 삽입
            
        # 2. 걷기 (1초 소요) - X-1, X+1
        for nxt_walk in [curr - 1, curr + 1]:
            if 0 <= nxt_walk <= 100000 and dist[nxt_walk] == -1:
                dist[nxt_walk] = dist[curr] + 1
                queue.append(nxt_walk) # 가중치가 1이므로 뒤쪽에 삽입

solve()
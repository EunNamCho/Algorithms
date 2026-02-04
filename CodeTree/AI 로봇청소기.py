"""
명세:
    1. N x N 행렬
    2. 좌상단 = (1,1)
    3. 각 칸은 1~100(먼지),0(빈칸),-1(물건)
    4. 로봇있는칸은 빈칸
    5. 청소기 이동:  (o)
        5-1. 이동거리 가장 가까운 오염된 지역으로 감
            -> 상하좌우? 아니면 대각선도 되는거임? -> 일단 상하좌우로만
        5-2. 물건, 청소기 있는 곳은 이동 불가
        5-3. 후보군 여러개면 작은 행, 작은 열로 이동
    6. 청소: (o)
        6-1. 본인 위치, 앞, 좌, 우 칸 청소가능
        6-2. 청소가능한 격자(4군데; 즉 영역을 의미) 중 먼지합이 가장 많은 영역부터
        6-3. 격자마다 최대 청소량 20
        6-4. 합이 같으면 오른쪽, 아래쪽, 왼쪽, 위쪽; 근데 방향이 앞쪽을 의미함. 그러니까 ㅏ 형태가 오른쪽, ㅜ가 아래쪽
        6-5. 청소는 청소기마다 순서대로 진행
    7. 먼지축적: (o)
        7-1. 먼지 있는 모든 격자에 +5
    8. 먼지확산: 
        8-1. 깨끗한 격자 주변 4방향 먼지량 합/10; 소숫점 버림
        8-2. 확산은 동시에
    9. 출력
        9-1. 전체 먼지량 출력
    10. 위 과정을 L번 반복
"""
from collections import deque
import functools

# input
N, K, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
robots = [list(map(lambda x: int(x)-1,input().split())) for _ in range(K)]
visited = [[-1]*N for _ in range(N)]
dirs = [(-1,0),(0,-1),(0,1),(1,0)]
regions = [[(0,0),(-1,0),(1,0),(0,1)],
           [(0,0),(0,-1),(0,1),(1,0)],
           [(0,0),(-1,0),(1,0),(0,-1)],
           [(0,0),(0,1),(0,-1),(-1,0)]]
robot_matrix = [[0]*N for _ in range(N)]
for r,c in robots:
    robot_matrix[r][c]=1

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print(f"[{func.__name__.upper()}]")
        result = func(*args, **kargs)
        show()
        print()
        return result
    return wrapper

def move(robot, idx):
    # print(idx, robot)
    # print(robot, robots)
    if matrix[robot[0]][robot[1]]>0:
        return robot
    
    queue = deque([robot])
    visited = [[-1]*N for _ in range(N)]
    visited[robot[0]][robot[1]] = idx
    while queue:
        r,c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            # print(nr,nc)
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]!=idx and matrix[nr][nc]!=-1 and not robot_matrix[nr][nc]:
                visited[nr][nc] = idx
                queue.append((nr,nc))
                if matrix[nr][nc]>0:
                    return nr,nc
    return -1,-1

from collections import deque

def move2(robot, idx):
    r0, c0 = robot

    # 현재 칸에 먼지가 있으면 이동 안 함
    if matrix[r0][c0] > 0:
        return robot

    # BFS 준비
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((r0, c0))
    dist[r0][c0] = 0

    # BFS로 reachable 여부 판정
    while q:
        r, c = q.popleft()

        for dr, dc in dirs:   # 상, 좌, 우, 하 (이 순서는 상관없음)
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] != -1:
                    continue
                if matrix[nr][nc] == -1:   # 물건
                    continue
                if robot_matrix[nr][nc]:  # 다른 로봇
                    continue

                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    # reachable한 오염 칸 중 최적 선택
    best = None        # (dist, r, c)
    best_dist = 10**9

    for r in range(N):
        for c in range(N):
            if matrix[r][c] > 0 and dist[r][c] != -1:
                d = dist[r][c]

                if d < best_dist:
                    best_dist = d
                    best = (r, c)
                elif d == best_dist:
                    # 행 우선 → 열 우선
                    if r < best[0]:
                        best = (r, c)
                    elif r == best[0] and c < best[1]:
                        best = (r, c)

    # 도달 가능한 오염 칸이 없다면 이동 불가
    if best is None:
        return (-1, -1)

    return best



def check_region(robot):
    # print(f"=check_region function at {robot}=")
    r,c = robot
    total = 0
    final_region = 0
    for idx, region in enumerate(regions):
        tmp = 0
        tmp2 = []
        for dr,dc in region:
            nr,nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]>=0:
                tmp+=matrix[nr][nc]
                tmp2.append((nr,nc))
        # print(f"region: {region}, sum: {tmp}")
        if total<tmp:
            total = tmp
            final_region = tmp2[:]
    return final_region

def check_region2(robot):
    r, c = robot
    best_sum = -1      # 먼지량 최대값
    best_idx = -1      # regions index
    best_region = None # 실제 청소할 좌표 리스트

    for idx, region in enumerate(regions):
        tmp_sum = 0
        coords = []

        for dr, dc in region:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] >= 0:
                tmp_sum += min(matrix[nr][nc],20)
                coords.append((nr, nc))

        # ------ tie-break logic ------
        # (1) 먼지량이 더 크면 무조건 선택
        if tmp_sum > best_sum:
            best_sum = tmp_sum
            best_idx = idx
            best_region = coords

        # (2) 먼지량 동일 → regions index가 더 작은 쪽 선택 (명세)
        elif tmp_sum == best_sum and idx < best_idx:
            best_idx = idx
            best_region = coords

    return best_region


def clean_region(robot,region):
    r,c = robot
    for nr,nc in region:
        matrix[nr][nc] = max(matrix[nr][nc]-20, 0)
        
# @debug
def plus_dust():
    for i in range(N):
        for j in range(N):
            if matrix[i][j]>0:
                matrix[i][j]+=5
                
# @debug 
def propagation():
    lazy = dict()
    for r in range(N):
        for c in range(N):
            if matrix[r][c]==0:
                total = 0
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<N and matrix[nr][nc]>0:
                        total+=matrix[nr][nc]
                total = total//10
                lazy[(r,c)] = total
    for (r,c), total in lazy.items():
        matrix[r][c] += total
    
def show():
    for row in matrix:
        for col in row:
            print(f"{col:>4}", end="")
        print()

def total_dust():
    total = 0
    for row in matrix:
        for col in row:
            if col>=0:
                total+=col
    return total

        
        
# show()
total = -1
for _ in range(L):
    if total==0:
        print(total)
        continue
    for idx, robot in enumerate(robots):
        # move
        nr,nc = move2(robot, idx)
        if nr==-1 and nc==-1:
            continue
        else:
            # print(f"[{idx}th robot move: {robot}->[{nr}, {nc}]]")
            robot_matrix[robot[0]][robot[1]] = 0
            robots[idx] = [nr,nc]
            robot_matrix[nr][nc]=1
            
    # print()
    
    for idx, robot in enumerate(robots):  
        # clean      
        # print(f"[{idx}th robot{robot} cleaning]")
        final_region = check_region2(robot)
        # print(f"Cleaning Target Region: {final_region}")
        if final_region==0:
            continue
        clean_region(robot, final_region)
    #     show()
    # print()
    
    # plus dust
    plus_dust()    
      
    # propagation
    propagation()
    
    # print
    total = total_dust()
    print(total)
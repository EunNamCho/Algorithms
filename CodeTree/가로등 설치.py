from collections import defaultdict
import heapq, math

# input
Q = int(input())
N, street = 0, []
adjacency = defaultdict(list)
order = []

for _ in range(Q):
    action = list(map(int, input().split()))
    if action[0]==100:
        N = action[1]
        M = action[2]
        lights = action[3:]
        order = action[3:]
        # print(lights, M)
        for idx, pos in enumerate(lights):
            # print(idx)
            # 앞뒤 관계 기록
            if 0<idx<(M-1):
                left = lights[idx-1]
                right = lights[idx+1]
            elif idx==0:
                left = -1
                right = lights[idx+1]
                adjacency["head"] = pos
            elif idx==(M-1):
                left = lights[idx-1]
                right = -1
                adjacency["tail"] = pos
            adjacency[pos].append(left)
            adjacency[pos].append(right)

            # 거리 측정
            if 0<idx<=(M-1):            
                dist = pos-left
                heapq.heappush(street, (-(dist),left,pos))
        # print(street)
        # print(adjacency)
    elif action[0]==200:
        while street:
            # print(street)
            dist, left, right = heapq.heappop(street)
            # print(dist,left,right)
            # print(street)
            # print(adjacency)
            # print(dist,left,right)
            if not adjacency[left]:
                continue
            elif not adjacency[right]:
                continue
            else:
                # heapq.heappush(street, (dist,left,right))
                break
        mid = math.ceil((left+right)/2)
        # print(left,right,mid)
        # print(mid-left-1, right-mid-1)
        if left==-1:
            pass
        elif right==-1:
            pass
        else:
            pass
        heapq.heappush(street, (-(mid-left),left,mid))
        adjacency[left][1] = mid
        adjacency[mid].append(left)
        heapq.heappush(street, (-(right-mid),mid,right))
        adjacency[right][0] = mid
        adjacency[mid].append(right)
        order.append(mid)
        # print(street)
        # print(adjacency)
    elif action[0]==300:
        tgt = order[action[1]-1]
        # print(order[action[1]-1])
        # print(street)
        # print(adjacency)
        left, right = adjacency[tgt]
        if adjacency["head"]==tgt:
            adjacency[right][0] = left
            adjacency["head"] = right
        elif adjacency["tail"]==tgt:
            adjacency[left][1] = right
            adjacency["tail"] = left
        else:
            dist = -(right-left)
            adjacency[right][0] = left
            adjacency[left][1] = right
            heapq.heappush(street, (dist,left,right))
        del adjacency[tgt]
        # print(street)
        # print(adjacency)
    elif action[0]==400:
        while street:
            # print(street)
            dist, left, right = heapq.heappop(street)
            # print(dist,left,right)
            # print(street)
            # print(adjacency)
            # print(dist,left,right)
            if not adjacency[left]:
                continue
            elif not adjacency[right]:
                continue
            else:
                heapq.heappush(street, (dist,left,right))
                break
            
        dist = -dist
        dist = dist/2
        # print(dist)
        if not adjacency[1]:
            dist = max(adjacency["head"]-1,dist)
            # print('here')
        if not adjacency[N]:
            dist = max(N-adjacency["tail"],dist)
            # print('here2')
        print(int(dist*2))
            
            
            
####################
from collections import defaultdict
import heapq, math
import sys
input = sys.stdin.readline

Q = int(input())

# 가로등 유효 여부
alive = dict()          # pos → True/False

# 가로등 연결 관계 (정확히 left, right 하나씩만 저장)
adj = dict()            # pos → [left, right]

# 모든 삽입 순서를 추적 (300 명령에서 사용)
order = []

# 내부 구간(왼쪽 pos, 오른쪽 pos, 길이)을 관리하는 최대 힙
# Python heap은 min-heap이므로 길이에 -를 붙여 저장
roads = []

# head / tail 은 딕셔너리 키로 넣지 않고, 명확하게 별도 변수로 관리
head = None
tail = None


def add_interval(l, r):
    """새 구간(l, r)을 roads 힙에 추가"""
    if l is None or r is None:
        return
    if not alive.get(l, False) or not alive.get(r, False):
        return
    length = r - l
    heapq.heappush(roads, (-length, l, r))


def is_valid_interval(l, r):
    """해당 interval이 현재 alive 상태와 adj 구조 상 실제로 존재하는지 확인"""
    if not alive.get(l, False): return False
    if not alive.get(r, False): return False
    # adj[l][1] == r 이고 adj[r][0] == l 이어야 유효
    return adj[l][1] == r and adj[r][0] == l


for _ in range(Q):
    action = list(map(int, input().split()))
    cmd = action[0]

    # ===============================
    # 초기 입력 (100)
    # ===============================
    if cmd == 100:
        N = action[1]
        M = action[2]
        lights = action[3:]

        lights.sort()

        # 초기화
        alive.clear()
        adj.clear()
        roads.clear()
        order = []

        for pos in lights:
            alive[pos] = True
            order.append(pos)

        # 연결 설정
        for i, pos in enumerate(lights):
            if i == 0:
                left = None
                right = lights[i+1] if M > 1 else None
                head = pos
            elif i == M-1:
                left = lights[i-1]
                right = None
                tail = pos
            else:
                left = lights[i-1]
                right = lights[i+1]

            adj[pos] = [left, right]

        # 내부 구간 heap 구성
        for i in range(M-1):
            add_interval(lights[i], lights[i+1])

    # ===============================
    # 삽입 (200)
    # ===============================
    elif cmd == 200:
        # 유효한 가장 긴 구간(pop)
        while roads:
            neg_len, l, r = heapq.heappop(roads)
            if is_valid_interval(l, r):
                break
        else:
            # 이 경우는 이상 상황이지만 문제 조건상 발생X
            continue

        # mid 계산
        mid = math.ceil((l + r) / 2)

        # 업데이트
        alive[mid] = True
        adj[mid] = [l, r]

        adj[l][1] = mid
        adj[r][0] = mid

        # old interval (l, r)은 자동 폐기(lazy)
        # 새 interval 2개 추가
        add_interval(l, mid)
        add_interval(mid, r)

        # head / tail 갱신 필요 X (중간 삽입)
        order.append(mid)

    # ===============================
    # 삭제 (300)
    # ===============================
    elif cmd == 300:
        idx = action[1] - 1
        tgt = order[idx]

        if not alive.get(tgt, False):
            continue  # 이미 삭제된 경우 무시 (정상적 입력이면 없음)

        l, r = adj[tgt]

        alive[tgt] = False
        del adj[tgt]

        # case 1: head 삭제
        if tgt == head:
            head = r
            if r is not None:
                adj[r][0] = None
        # case 2: tail 삭제
        elif tgt == tail:
            tail = l
            if l is not None:
                adj[l][1] = None
        else:
            # 중간 삭제 → 새 interval (l, r) 생성
            adj[l][1] = r
            adj[r][0] = l
            if l is not None and r is not None:
                add_interval(l, r)

        # order 리스트는 그대로 두어도 됨 (삭제 시 순서 참조만)

    # ===============================
    # 전력 계산 (400)
    # ===============================
    elif cmd == 400:

        # 1) 가장 긴 내부 구간 찾기
        longest = 0
        while roads:
            neg_len, l, r = heapq.heappop(roads)
            if is_valid_interval(l, r):
                longest = -neg_len
                heapq.heappush(roads, (neg_len, l, r))
                break

        # 2) head 왼쪽 공간
        left_gap = 0
        if head is not None:
            left_gap = (head - 1) * 2

        # 3) tail 오른쪽 공간
        right_gap = 0
        if tail is not None:
            right_gap = (N - tail) * 2

        result = max(longest, left_gap, right_gap)
        print(result)

"""
1. 명령 시퀀스 하나씩 순회
2. 현재 명령어가 U,R,L,D 중 무엇인지 확인
3. dict[((src, dst),(dst,src))] and 반대가 있는지 확인
4. 없으면 answer += 1 and 추가.
"""
from collections import defaultdict
def solution(dirs):
    answer = 0
    src_dst = defaultdict()
    cur_x = cur_y = 0 # x,y
    for d in dirs:
        if d=="U":
            next_x, next_y = cur_x, cur_y+1
        elif d=="D":
            next_x, next_y = cur_x, cur_y-1
        elif d=="R":
            next_x, next_y = cur_x+1, cur_y
        elif d=="L":
            next_x, next_y = cur_x-1, cur_y
        if -5<=next_x<=5 and -5<=next_y<=5:
            if src_dst.get(((cur_x,cur_y),(next_x,next_y))) is None:
                src_dst[((cur_x,cur_y),(next_x,next_y))] = 1
                src_dst[((next_x,next_y),(cur_x,cur_y))] = 1
                answer+=1              
            cur_x, cur_y = next_x, next_y
    return answer

def solution(dirs):
    # 방향 벡터
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    x, y = 0, 0
    visited_edges = set()
    ans = 0

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        # 경계 밖이면 무시
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        # 무방향 간선 표현 (방향 제거)
        a = (x, y)
        b = (nx, ny)
        edge = (a, b) if a <= b else (b, a)

        if edge not in visited_edges:
            visited_edges.add(edge)
            ans += 1

        x, y = nx, ny

    return ans

# 함수쓰니까 훨씬 빨라짐.
"""
✅ 1. 지역 변수(Local Variables)가 더 빠르다
Python은 지역 변수 접근이 전역 변수나 바깥 스코프 변수 접근보다 훨씬 빠름.

함수 안에서 쓰는 변수는 C로 구현된 로컬 변수 배열에서 직접 인덱싱됨.

반면 함수 밖의 변수는 딕셔너리 기반의 글로벌/클로저 영역에서 찾기 때문에 느림.

python
복사
편집
# 함수 밖에서 리스트 접근
for _ in range(10000000): x = a[0]  # 느림

# 함수 안에서 리스트 접근
def f(): 
    for _ in range(10000000): x = a[0]  # 빠름
💡 BFS에서 visited, queue, I, 좌표값 등 수십만 번 접근되기 때문에, 이 차이가 누적되면 꽤 큼.

✅ 2. 루프 변수의 바인딩 속도
함수 안에서 반복문을 돌릴 때, Python은 loop variable (for x in ...)도 내부적으로 로컬 변수 바인딩을 사용해서 성능이 더 좋음.

전역 루프는 매 루프마다 globals() 딕셔너리를 참조해야 하고,

로컬 루프는 그냥 C 배열에서 인덱싱만 하면 됨.

✅ 3. 컴파일러 최적화 (CPython level)
CPython 인터프리터는 함수 안의 코드를 LOAD_FAST, STORE_FAST 같은 빠른 바이트코드를 써서 컴파일함.

반면 함수 밖에서는 LOAD_NAME, LOAD_GLOBAL 등 더 느린 명령을 써야 해.

python
복사
편집
# dis 모듈로 비교해보면
dis.dis("x = a + b")  # 전역에서는 LOAD_NAME
def f(): x = a + b
dis.dis(f)            # 함수 안에서는 LOAD_FAST
📉 결국 동일한 연산을 해도 전역보다 지역에서 훨씬 빠르게 실행됨.

✅ 4. 변수 수명 관리도 더 효율적
함수 안에서 쓰는 변수들은 함수 호출이 끝나면 바로 GC 대상이 되기 쉽고,
전역 변수는 오랫동안 메모리에 남아 있어서 불필요한 메모리 유지가 발생할 수도 있어.

✅ 정리: 왜 함수가 빠른가?
이유	함수 안 (빠름)	함수 밖 (느림)
변수 접근 방식	LOAD_FAST	LOAD_GLOBAL / LOAD_NAME
메모리 구조	배열 인덱스 접근	딕셔너리 해시 접근
루프 성능	최적화 쉬움	상대적으로 느림
가비지 컬렉션	수명 짧고 관리 쉬움	메모리 오래 유지
✨ 결론
Python에서는 같은 코드를 함수로 감싸기만 해도 성능이 눈에 띄게 좋아지는 경우가 꽤 많아. 특히 반복이 많거나 BFS/DFS 같은 알고리즘에선 지역 변수의 이점이 크기 때문이야.
"""

import sys
from collections import defaultdict, deque

# input
T = int(sys.stdin.readline().strip())
dirs = [(-2,1),(-1,2),(1,2),(2,1),
        (2,-1),(1,-2),(-1,-2),(-2,-1)]

def bfs(src_y,src_x,dst_y,dst_x):
    visited = [[0]*I for _ in range(I)]

    # algorithm - BFS
    queue = deque([(src_y, src_x)])
    while queue:
        cur_y, cur_x = queue.popleft()
        if cur_y==dst_y and cur_x==dst_x:
            return visited[cur_y][cur_x]
        for dy, dx in dirs:
            new_y, new_x = cur_y+dy, cur_x+dx
            if (0<=new_y<I) and (0<=new_x<I) and not visited[new_y][new_x]:
                queue.append((new_y,new_x))
                visited[new_y][new_x] = visited[cur_y][cur_x] + 1

for _ in range(T):
    I = int(sys.stdin.readline().strip())
    src_y, src_x = map(int, sys.stdin.readline().strip().split())
    dst_y, dst_x = map(int, sys.stdin.readline().strip().split())
    # visited = [[0]*I for _ in range(I)]

    # algorithm - BFS
    # queue = deque([(src_y, src_x)])
    # while queue:
    #     cur_y, cur_x = queue.popleft()
    #     if cur_y==dst_y and cur_x==dst_x:
    #         break
    #     for dy, dx in dirs:
    #         new_y, new_x = cur_y+dy, cur_x+dx
    #         if (0<=new_y<I) and (0<=new_x<I) and not visited[new_y][new_x]:
    #             queue.append((new_y,new_x))
    #             visited[new_y][new_x] = visited[cur_y][cur_x] + 1
        # print("=")
        # for row in visited:
        #     print(row)

    # output
    # print(visited[dst_y][dst_x])
    print(bfs(src_y,src_x,dst_y,dst_x))
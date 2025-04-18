# 나는 풀 줄 몰라서 matrix로 하나하나 색칠하려고 했는데, 아래처럼 간결한 방식이 있네.
"""
✅ 추천 해결 방법 (일반적인 백트래킹 방식)
이 문제는 행 단위로 퀸을 배치하는 방식이 일반적이야.
즉, 한 행에 하나의 퀸만 놓고, 다음 행으로 넘어가는 식이야.

보통은 다음 세 가지 배열로 체크해:

cols = [False] * N  # 열 사용 여부
diag1 = [False] * (2*N)  # '/' 방향 대각선
diag2 = [False] * (2*N)  # '\' 방향 대각선

1️⃣ 왜 2*N 길이의 배열을 쓰는가?
각 방향의 대각선 개수는 최대 2N-1개이기 때문이야.

체스판에서 / 방향 (↙↗ 방향)은 왼쪽 위에서 오른쪽 아래로 줄을 세면 총 2N-1개.

\ 방향 (↖↘ 방향)도 마찬가지로 2N-1개.

Python에서 인덱스를 0부터 쓰니까 배열 크기를 2*N으로 넉넉히 할당하는 것뿐이야.

예: N=4일 때

\ 대각선 인덱스 번호:
3 2 1 0
4 3 2 1
5 4 3 2
6 5 4 3 

/ 대각선 인덱스 번호:
0 1 2 3
1 2 3 4
2 3 4 5
3 4 5 6
"""

import sys
sys.setrecursionlimit(10000000)

# input
N = int(sys.stdin.readline())
answer = [0]
columns = [False] * N
left_diag = [False] * (2*N-1) # \ diag
right_diag = [False] * (2*N-1) # / diag

# algorithm - Backtracking
def back(row):
    if row==N:
        answer[0] += 1
        return
    
    for col in range(N):
        if not columns[col] and not right_diag[row+col] and not left_diag[N+row-col-1]:
            columns[col] = right_diag[row+col] = left_diag[N+row-col-1] = 1
            back(row+1)
            columns[col] = right_diag[row+col] = left_diag[N+row-col-1] = 0
# if N==14: print(365596)
# else:
back(0)
print(answer[0])
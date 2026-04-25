import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    
    # Algorithm - Backtracking
    left_diag = [False]*(2*N-1)
    right_diag = [False]*(2*N-1)
    diag = defaultdict(list)
    
    for i in range(2*N-1):
        r,c = min(i,N-1),max(0,i-N+1)
        # if i<=N-1:
        #     r,c = i,0
        # else:
        #     r,c = N-1,i-N+1
        # while True:         
        #     if 0<=r<N and 0<=c<N:
        #         if matrix[r][c]:
        #             diag[i].append((r,c))
        #     else:
        #         break
        #     r,c = r-1,c+1
        while 0<=r<N and 0<=c<N:
            if matrix[r][c]:
                diag[i].append((r,c))
            r,c = r-1,c+1
            
    # for i in range(2*N-1):
    #     print(diag[i])
    
    def back(i,tmp):
        nonlocal answer
        if i==2*N-1:
            answer = max(answer,tmp)
            return
        for r,c in diag[i]:
            if not right_diag[r+c] and not left_diag[N-r+c-1]:
                right_diag[r+c] = left_diag[N-r+c-1] = True
                back(i+1,tmp+1)
                right_diag[r+c] = left_diag[N-r+c-1] = False
        back(i+1,tmp)
        
    back(0,0)
    print(answer)
    
main()


import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # Algorithm - Backtracking
    diag = defaultdict(list)
    
    # / 방향 대각선별로 비숍을 놓을 수 있는 칸 모으기
    for i in range(2 * N - 1):
        r, c = min(i, N - 1), max(0, i - N + 1)
        while 0 <= r < N and 0 <= c < N:
            if matrix[r][c]:
                diag[i].append((r, c))
            r, c = r - 1, c + 1

    def solve(start):
        right_diag = [False] * (2 * N - 1)   # \ 방향 대각선 사용 여부
        best = 0

        def back(i, cnt):
            nonlocal best
            if i >= 2 * N - 1:
                best = max(best, cnt)
                return

            for r, c in diag[i]:
                idx = r - c + N - 1   # \ 방향 대각선 인덱스
                if not right_diag[idx]:
                    right_diag[idx] = True
                    back(i + 2, cnt + 1)
                    right_diag[idx] = False

            back(i + 2, cnt)

        back(start, 0)
        return best

    answer = solve(0) + solve(1)
    print(answer)

main()
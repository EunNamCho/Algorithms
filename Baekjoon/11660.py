import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    
    # 원본 배열
    arr = [[0] * (N + 1)]
    for _ in range(N):
        arr.append([0] + list(map(int, input().split())))
    
    # 2차원 누적합 배열
    psum = [[0] * (N + 1) for _ in range(N + 1)]
    
    # 누적합 계산
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            psum[i][j] = (
                arr[i][j]
                + psum[i - 1][j]
                + psum[i][j - 1]
                - psum[i - 1][j - 1]
            )
    
    # 쿼리 처리
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        result = (
            psum[x2][y2]
            - psum[x1 - 1][y2]
            - psum[x2][y1 - 1]
            + psum[x1 - 1][y1 - 1]
        )
        print(result)

main()

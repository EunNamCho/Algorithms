import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = list(map(int, input().split()))

    inc = [1] * N
    dec = [1] * N

    # LIS (왼쪽 → 오른쪽)
    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + 1)

    # LDS (오른쪽 → 왼쪽)
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if arr[j] < arr[i]:
                dec[i] = max(dec[i], dec[j] + 1)

    answer = 0
    for i in range(N):
        answer = max(answer, inc[i] + dec[i] - 1)

    print(answer)

main()
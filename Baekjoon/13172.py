import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    M = int(input())
    answer = 0

    for _ in range(M):
        N, S = map(int, input().split())

        g = gcd(N, S)
        N //= g
        S //= g

        inv = pow(N, MOD - 2, MOD)
        answer = (answer + S * inv) % MOD

    print(answer)

main()
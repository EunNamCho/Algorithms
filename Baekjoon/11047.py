import sys

# input
N, K = map(int, sys.stdin.readline().strip().split())
coins = []
answer = 0
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

# algorithm - BruteForce
for i in range(1,N+1):
    coin = coins[-i]
    if K < coin:
        continue
    q, K = divmod(K, coin)
    answer += q
print(answer)
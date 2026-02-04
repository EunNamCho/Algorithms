import sys
input = sys.stdin.readline
write = sys.stdout.write

# Input
T = int(input())

# Algorithm - DP
answer = []
zeros, ones = [-1]*41, [-1]*41
zeros[0] = 1
zeros[1] = 0
ones[1] = 1
ones[0] = 0
for _ in range(T):
    N = int(input())
    for i in range(N+1):
        if zeros[i]==-1:
            zeros[i] = zeros[i-1]+zeros[i-2]
        if ones[i]==-1:
            ones[i] = ones[i-1]+ones[i-2]
    answer.append(f"{zeros[N]} {ones[N]}")

write("\n".join(answer))
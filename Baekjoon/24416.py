import sys

# input
N = int(sys.stdin.readline())

# algoirhtm - None
fib = [0] * (N + 1)
fib[1] = fib[2] = 1
for i in range(3, N + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

print(fib[N] ,N-2)
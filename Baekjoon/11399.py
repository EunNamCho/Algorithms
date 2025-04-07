import sys

# input
N = int(sys.stdin.readline().strip())
wait_times = list(map(int, sys.stdin.readline().strip().split()))
answer = 0

# algorithm
wait_times.sort()
for i, _ in enumerate(wait_times):
    answer += sum(wait_times[:i+1])

# output
print(answer)
import sys
input = sys.stdin.readline
write = sys.stdout.write

# Input
N, M = map(int, input().rstrip().split())
numbers = list(map(int,input().rstrip().split()))
outputs = []

# Algorithm - Prefix Sum
prefix = [0,numbers[0]]
for number in numbers[1:]:
    prefix.append(prefix[-1]+number)

for _ in range(M):
    i, j = map(int, input().rstrip().split())
    outputs.append(str(prefix[j]-prefix[i-1]))

write("\n".join(outputs))

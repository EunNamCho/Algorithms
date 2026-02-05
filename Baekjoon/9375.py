import sys
from collections import defaultdict
input = sys.stdin.readline
write = sys.stdout.write

# Input
T = int(input())
outputs = []

# Algorithm - Implementation
for _ in range(T):
    closet = defaultdict(int)
    answer = 1
    n = int(input())
    for _ in range(n):
        _, category = input().rstrip().split()
        closet[category]+=1
    
    for number in closet.values():
        answer *= (number+1)
    
    if n==0:
        outputs.append(str(0))
    else:
        outputs.append(str(answer-1))

write("\n".join(outputs))
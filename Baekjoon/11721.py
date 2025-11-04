import sys

# input
S = sys.stdin.readline().strip()

# algorithm - Implementation
tmp = ""
for s in S:
    tmp+=s
    if len(tmp)==10:
        print(tmp)
        tmp = ""
print(tmp)
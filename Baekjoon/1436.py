import sys

# input
N = int(sys.stdin.readline())

# Algorithm - BruteForce
start = 666
cnt = 0
while True:
    if '666' in str(start):
        cnt += 1
    if cnt==N:
        print(start)
        break
    start += 1

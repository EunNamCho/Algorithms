# 11M
import sys

# input
N = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
galons = list(map(int, sys.stdin.readline().split()))

# alogirhtm - Greedy
def greedy():
    cnt = 0
    cheapest = float("inf")

    for idx in range(N-1):
        if idx==0:
            cnt += galons[idx]*roads[idx]
            cheapest = galons[idx]
        else:
            if cheapest <= galons[idx]:
                cnt += cheapest*roads[idx]
            else:
                cnt += galons[idx]*roads[idx]
                cheapest = galons[idx]
    return cnt

print(greedy())
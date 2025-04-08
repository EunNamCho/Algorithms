import sys

# input
N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# algorithm - Greedy
def greedy():
    meetings.sort(key=lambda x:(x[1],x[0]))
    cnt = 0
    end_time = 0

    for start, end in meetings:
        if start >= end_time:
            cnt += 1
            end_time = end
    return cnt
    
print(greedy())
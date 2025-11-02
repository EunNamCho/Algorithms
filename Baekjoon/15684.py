import sys

# input 
N,M,H = map(int, sys.stdin.readline().split())
lanes = [[0]*(N-1) for _ in range(H)] # 0=>0~1, 1=>1~2 ...
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    lanes[b-1][a-1] = 1

# input check
print(lanes)

# algorithm - Backtracking
def check():
    global lanes
    for i,row in enumerate(lanes):
        for col in enumerate(row):
            if col==1 and 

def back():
    pass
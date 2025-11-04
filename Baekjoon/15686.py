import sys

# input
N,M = map(int, sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
houses = []
chickens = []
answer = float("inf")
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col==1:
            houses.append([i,j])
        elif col==2:
            chickens.append([i,j])

# algorithm - Backtracking
def distance(selected):
    global houses,answer
    d = 0
    for hr,hc in houses:
        tmp = float("inf")
        for sr,sc in selected:
            tmp = min(tmp,abs(hr-sr)+abs(hc-sc))
        d += tmp
        if d>answer:
            break
    return d

def back(selected, idx):
    global N,M,chickens,answer
    if len(selected)+(len(chickens)-idx) < M:
        return
    if len(selected)==M:
        d = distance(selected)
        answer = min(answer, d)
        return
    
    for i in range(idx, len(chickens)):
        back(selected+[chickens[i]],i+1)

back([],0)
print(answer)
import sys
from itertools import combinations

# input
N = int(sys.stdin.readline())
matrix = []
visited = [False] * N
diff = [float("inf")]
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# algorithm - Backtrakcing
def back(idx, team):
    # term
    if len(team)==N//2:
        link_team = []
        for person, belong in enumerate(visited):
            if not belong:
                link_team.append(person)
        # print(team,link_team)
        # calc
        star = link = 0
        for y,x in combinations(team,2):
            star += (matrix[y][x]+matrix[x][y])
        for y,x in combinations(link_team,2):
            link += (matrix[y][x]) + (matrix[x][y])
        diff[0] = min(diff[0], abs(star-link))
        if diff[0]==0:
            print(0)
            sys.exit(0)
        return

    if idx >= N:
        return 
    
    for person in range(idx, N):
        if not visited[person]:
            team.append(person)
            visited[person] = True
            back(idx+1, team)
            team.pop()
            visited[person] = False

back(0, [])
print(diff[0])
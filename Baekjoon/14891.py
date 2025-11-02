import sys
from collections import deque

# input 
gears = [0] # List[Deque[int]] N:0, S:1
for _ in range(4):
    tmp = sys.stdin.readline().strip()
    gear = deque()
    for polar in tmp:
        if polar=="1":
            gear.append(1)
        else:
            gear.append(0)
    gears.append(gear)
K = int(sys.stdin.readline())
operations = [list(map(int,sys.stdin.readline().split())) for _ in range(K)] # List[List[int]] num, direction clock:1, c-clock:-1

# algorithm - Implementation
def rotate(gear, direction):
    # print("Direction: ", direction)
    # print("Before rotation: ", gear)
    if direction==1:
        gear.appendleft(gear.pop())
    elif direction==-1:
        gear.append(gear.popleft())
    # print("After rotation: ", gear)
    return gear
        
def Imple():
    global gears,operations
    answer = 0
    """
        회전할 때 다른 극이면 반대방향으로 회전. 같으면 가만히.
        1번의 회전은 diff[0]확인
        2번의 회전은 diff[0], diff[1]확인
        3번의 회전은 diff[1], diff[2]확인
        4번의 회전은 diff[2]확인
        
        1st gear: if 12=>N: 0pt, else: 1pt
        2nd gear: if 12=>N: 0pt, else: 2pt
        3rd gear: if 12=>N: 0pt, else: 4pt
        4th gear: if 12=>N: 0pt, else: 8pt
    """
    for operation in operations:
        num, direction = operation
        rotated = [0]*5
        rotated[num] = direction
        # print(f"Start from {num}th gear, {direction} direction")
        # left chain reaction
        for i in range(num,1,-1):
            # print(i)
            if rotated[i] and gears[i][-2]!=gears[i-1][2]:
                rotated[i-1] = -rotated[i]
        # print(f"After Left chain reaction: {rotated}")
        # right chain reaction
        for i in range(num,4):
            # print(i)
            if rotated[i] and gears[i][2]!=gears[i+1][-2]:
                rotated[i+1] = -rotated[i]
        # print(f"After Right chain reaction: {rotated}")
                
        for i in range(1,5):
            gears[i] = rotate(gears[i],rotated[i])
        
    print(gears[1][0]*1+gears[2][0]*2+gears[3][0]*4+gears[4][0]*8)

Imple()

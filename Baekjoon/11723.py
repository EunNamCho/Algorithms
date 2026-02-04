import sys 
input = sys.stdin.readline

# input
M = int(input().strip())
S = 0

# Algorithm - Implementation
for _ in range(M):
    cmd = input().split()
    
    if cmd[0]=="add":
        S |= 1<<(int(cmd[1])-1)
    elif cmd[0]=="remove":
        S &= ~(1<<(int(cmd[1])-1))
    elif cmd[0]=="check":
        if S & (1<<(int(cmd[1])-1)):
            print(1)
        else:
            print(0)
    elif cmd[0]=="toggle":
        S ^= 1<<(int(cmd[1])-1)
    elif cmd[0]=="all":
        S = (1<<21)-1
    elif cmd[0]=="empty":
        S = 0
    
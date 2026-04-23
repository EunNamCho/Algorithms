import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    S = input().rstrip()
    answer = []
    
    # Algorithm - Implementation
    flip = True
    tmp = deque()
    for s in S:
        if s=="<":
            flip = False
        if flip:
            if s==" ":
                tmp.append(" ")
                answer.append(tmp)
                tmp = deque()
            else:
                tmp.appendleft(s)
        else:
            tmp.append(s)
        if s==">":
            flip = True
            answer.append(tmp)
            tmp = deque()
    if tmp:
        answer.append(tmp)
    # print(answer)
    for s in answer:
        if isinstance(s,deque):
            print("".join(s),end="")      
main()
import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    M = int(input())
    text = input().rstrip()
    answer = 0
    
    # Algorithm - Implementation
    start = False
    next = "I"
    zeros = 0
    for i,char in enumerate(text):
        if not start:
            if char=="I":
                start = True
                next = "O"
        else:
            if char==next:
                if char=="O":
                    zeros += 1
                    next = "I"
                else:
                    if zeros==N:
                        zeros = 0
                        answer += 1
                    next = "O"
            else:
                if char=="I":
                    zeros = 0
                    next = "O"
                else:
                    start = False
                    zeros = 0
                    next = "I"
        # print(i,char,start,next,zeros,answer)
    print(answer)
                    
main()
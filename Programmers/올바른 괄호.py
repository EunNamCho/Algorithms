from collections import deque

def solution(s):
    answer = False
    queue = deque()
    for char in s:
        if not queue:
            queue.append(char)
        else:
            if queue[-1]==char:
                queue.append(char)
            else:
                if queue[-1]=="(":
                    queue.pop()
                else:
                    queue.append(char)
    if not queue:
        answer = True
    return answer


def solution(s):
    queue = 0
    for char in s:
        if char=="(":
            queue+=1
        else:
            queue-=1
        if queue<0:
            return False
    if queue>0:
        return False
    return True

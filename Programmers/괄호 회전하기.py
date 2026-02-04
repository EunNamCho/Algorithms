from collections import deque
def solution(s):
    OPEN = ["(", "[", "{"]
    PAIRS = {")":"(", "]":"[", "}":"{"}
    def check(s):
        # print(s)
        stack = []
        for char in s:
            if char in OPEN:
                stack.append(char)
            else:
                if stack and stack[-1]==PAIRS[char]:
                    stack.pop()
                else:
                    return False
        return not stack
    
    string = deque([char for char in s])
    # print(len(string))
    answer = 0
    for i in range(len(string)):
        string.append(string.popleft())
        # print(i+1,string,check(string))
        if check(string):
            answer += 1
    return answer
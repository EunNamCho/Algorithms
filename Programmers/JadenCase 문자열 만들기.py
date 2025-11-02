def solution(s):
    answer = ""
    cap = True
    for char in s:
        if char==" ":
            answer += char
            cap = True
        else:
            if cap:
                answer += char.upper()
                cap = False
            else:
                answer += char.lower()
    return answer
def solution(s):
    answer = [0,0]
    while True:
        tmp = ""
        for char in s:
            if char=="0":
                answer[1]+=1
            else:
                tmp+=char
        c = len(tmp)
        s = bin(c)[2:]
        answer[0]+=1
        if s=="1":
            return answer
        
def solution(s):
    cnt_bin, cnt_zero = 0, 0
    while s != "1":
        cnt_zero += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
        cnt_bin += 1
    return [cnt_bin, cnt_zero]

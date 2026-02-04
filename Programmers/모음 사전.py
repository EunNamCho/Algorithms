def back(n, word,tgt):
    if word==tgt:
        print(n)
        return n
    # if len(word)==5:
    #     return n, False
    for ch in ["A", "E", "I", "O", "U"]:
        if len(word)<5:
            back(n+1,word+ch,tgt)
        else:
            pass

def solution(word):
    answer = 0
    print(back(0,"",word))

solution("AAAAE")
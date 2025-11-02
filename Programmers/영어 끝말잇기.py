def solution(n, words):
    word_count = dict()
    turn = 1
    i = 2
    person = 2
    prev_word = words[0]
    cur_word = words[1]
    word_count[prev_word]=1
    print(words)
    while True:
        # print(prev_word,cur_word)
        if prev_word[-1]==cur_word[0]:
            if word_count.get(cur_word) is None:
                word_count[cur_word] = 1
            else:
                return [person,turn]
        else:
            return [person,turn]
        person +=1
        i+=1
        if person>n:
            person=1
            turn+=1
        if i>len(words): break
        prev_word, cur_word = cur_word, words[i-1]
    return [0,0]

def solution(n, words):
    duplicated = set([words[0]])
    
    for i in range(1,len(words)):
        prev, cur = words[i-1],words[i]
        person, turn = i%n+1, i//n+1
        print(prev,cur,person,turn)
        if prev[-1]==cur[0]:
            if cur not in duplicated:
                duplicated.add(cur)
            else:
                return [person,turn]
        else:
            return [person,turn]
    return [0,0]


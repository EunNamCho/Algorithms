def solution(s):
    answer = []
    tuples = dict()
    tuple = []
    number = ""
    start = True
    for char in s:
        if char.isnumeric():
            number+=char
        else:
            if number:
                number = int(number)
                tuple.append(number)
                number = ""
            if char=="}" and tuple:
                tuples[len(tuple)]=tuple
                tuple = []
            
    # print(tuples)
    for i in range(1,len(tuples)+1):
        for number in tuples[i]:
            if number not in answer:
                answer.append(number)
    return answer


def solution(s):
    groups = {}
    cur = []
    number = ""

    for ch in s:
        if ch.isnumeric():
            number += ch
        else:
            if number:
                cur.append(int(number))
                number = ""
            if ch == "}" and cur:
                groups[len(cur)] = cur
                cur = []

    answer = []
    seen = set()
    for size in range(1, len(groups) + 1):
        for num in groups[size]:
            if num not in seen:
                seen.add(num)
                answer.append(num)
    return answer


def solution(s):
    # 바깥 {{ , }} 제거 후 "2},{2,1},{2,1,3},{2,1,3,4" 꼴로 만듦
    parts = s[2:-2].split("},{")
    # 길이(원소 개수) 순으로 정렬
    parts.sort(key=len)
    print(parts)

    answer = []
    seen = set()

    for part in parts:
        for num in map(int, part.split(',')):
            if num not in seen:
                seen.add(num)
                answer.append(num)

    return answer

def solution(numbers):
    answer = [0]*len(numbers)
    find = []

    for idx, number in enumerate(numbers):
        if not find:
            find.append((number,idx))
        else:
            if find[-1][0] >= number:
                find.append((number,idx))
            else:
                while find and find[-1][0] < number:
                    num, i = find.pop()
                    answer[i] = number
                find.append((number,idx))
    while find: 
        num, i = find.pop()
        answer[i] = -1
    return answer
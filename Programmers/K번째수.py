def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer
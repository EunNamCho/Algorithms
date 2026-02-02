def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for idx, char in enumerate(word):
        weight = pow(5, 4-idx)
        coeff = vowels.index(char)
        answer += weight * coeff + 1
    return answer
        

    
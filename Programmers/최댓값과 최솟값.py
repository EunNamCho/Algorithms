def solution(s):
    answer = ''
    numbers = list(map(int,s.split()))
    numbers.sort()
    answer = f"{numbers[0]} {numbers[-1]}"
    return answer

if __name__=="__main__":
    print(solution("-1 -2 -3 -4"))
def solution(people: int, limit: int)->int:
    answer = 0
    people.sort()
    left,right = 0,len(people)-1
    while left<=right:
        if people[left]+people[right]<=limit:
            left += 1
        right -= 1
        answer += 1
    return answer

if __name__=="__main__":
    print(solution([70,50,80,50],100))
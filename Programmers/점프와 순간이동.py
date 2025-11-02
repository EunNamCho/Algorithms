def solution(n):
    answer = 0
    
    while n!=0:
        q,r = divmod(n,2)    
        if r!=0:
            answer += 1
        n=q
    return answer
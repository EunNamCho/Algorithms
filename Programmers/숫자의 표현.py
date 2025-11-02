def solution(n):
    answer = 0
    left = right = 1
    current = 1
    while left<=right:
        if current==n:
            answer += 1
            current -= left
            left += 1
        elif current<n:
            right += 1
            current += right
            if right > n:
                break
        else:
            current -= left
            left += 1          
    return answer

if __name__=="__main__":
    print(solution(15))
    
def solution(n: int) -> int:
    # 2의 거듭제곱 인자 제거
    while n % 2 == 0:
        n //= 2
    # 남은 홀수 m의 약수 개수 계산
    ans = 1
    p = 3
    m = n
    cnt = 0
    # 3부터 sqrt까지 소인수 분해
    while p * p <= m:
        cnt = 0
        while m % p == 0:
            m //= p
            cnt += 1
        if cnt:
            ans *= (cnt + 1)
        p += 2
    if m > 1:  # 마지막 소인수
        ans *= 2
    return ans

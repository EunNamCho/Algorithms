import math

# 1: (1)
# 2: (1,1), (2)
# 3: (1,1,1),(2,1),(1,2)
# 4: (1,1,1,1),(2,1,1),(1,2,1),(1,1,2),(2,2)
# 5: (1,1,1,1,1),(2,1,1,1),(1,2,1,1),(1,1,2,1),(2,2,1),(1,1,1,2),(2,1,2),(1,2,2)
# 6: (1,1,1,1,1,1),(2,1,1,1,1),(1,2,1,1,1),(1,1,2,1,1),(2,2,1,1),(1,1,1,2,1),(2,1,2,1),(1,2,2,1),()
def solution(n):
    answer = 1
    i = 1
    while 2*i<=n:
        l = n-i
        answer = (answer+(math.factorial(l)//(math.factorial(i)*math.factorial(l-i))))%1234567#lCi
        answer = (answer+math.comb(l,i))%1234567#lCi
        i+=1
    return answer%1234567

def solution(n):
    a,b = 1,2
    if n==1:
        return 1
    if n==2:
        return 2
    i=2
    while True:
        a,b = b,(a+b)%1234567
        i+=1
        if i==n:
            break
    return b
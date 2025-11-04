import math

def solution(n):

    ans = float("inf")
    i = 1
    while True:
        q,r = divmod(n,pow(i,2))
        print(q,r)
        i += 1
        ans = min(ans,q+r)
        if q == 0:
            break

    return ans
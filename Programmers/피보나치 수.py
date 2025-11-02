import sys
sys.setrecursionlimit(10000000)
def solution(n):
    fibos = [0]*100_001
    fibos[1]=1
    def fibo(n):
        if n==0 or n==1: return fibos[n]
        else:
            if fibos[n]==0:
                fibos[n] = (fibo(n-1) + fibo(n-2))%1234567
            return fibos[n]
    return fibo(n)

def solution(n: int) -> int:
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1234567
    return b

import math
from functools import reduce

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a    

def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        # g = math.gcd(answer,num)
        g = gcd(answer,num)
        answer = answer*num//g
    return answer

def solution(arr):
    def lcm(a,b):
        return a*b//gcd(a,b)
    return reduce(lcm, arr)
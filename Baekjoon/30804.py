import sys
from collections import defaultdict
input = sys.stdin.readline

# Input
N = int(input())
fruits = list(map(int,input().split()))

# Algorithm - TwoPointer
left, right = 0, 0
count = defaultdict(int)
count[fruits[left]] += 1
answer = 1

while left<=right: 
    if len(count)<=2:
        answer = max(answer, right-left+1)
        if right<N-1:
            right += 1
            count[fruits[right]] += 1
        else:
            break
    else:
        count[fruits[left]] -= 1
        if count[fruits[left]]==0:
            del count[fruits[left]]
        left += 1
    # print(fruits[left:right+1])
        
print(answer)
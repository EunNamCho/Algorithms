import sys
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
max_height = 0
trees = list(map(int,input().split()))

# Algorithm - Binary Search
min_h, max_h = 0, max(trees)
answer = 0

while min_h<max_h:
    half = min_h+int((max_h-min_h)/2+0.5)
    
    remain = 0
    for tree in trees:
        tmp = tree - half
        if tmp>0:
            remain += tmp
            
    # print(min_h,max_h,answer,half,remain)
            
    if remain > M:
        answer = max(answer,half)
        min_h = half
    elif remain < M:
        max_h = half
    elif remain==M or (max_h-min_h)==1:
        answer = half
        break
        
print(answer)
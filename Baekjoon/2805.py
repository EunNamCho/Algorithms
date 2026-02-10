import sys
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
max_height = 0
trees = list(map(int,input().split()))

# Algorithm - Binary Search
min_h, max_h = 0, max(trees)
answer = 0

while min_h<=max_h:
    half = min_h+(max_h-min_h)//2
    
    remain = 0
    for tree in trees:
        if tree>half:
            remain += tree-half
            
    # print(min_h,max_h,answer,half,remain)
            
    if remain >= M:
        answer = max(answer,half)
        min_h = half+1
    elif remain < M:
        max_h = half-1
        
print(answer)


import sys

def solve():
    # 입력 속도를 높이기 위해 sys.stdin.read 사용
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])  # 나무의 수
    m = int(input[1])  # 필요한 나무 길이
    trees = list(map(int, input[2:]))
    
    start, end = 0, max(trees)
    result = 0
    
    # 이분 탐색 시작
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        # mid 높이로 잘랐을 때 가져갈 수 있는 나무 계산
        for tree in trees:
            if tree > mid:
                total += tree - mid
                
        # 나무의 양이 충분한 경우 (최대한 높이를 높여야 함)
        if total >= m:
            result = mid
            start = mid + 1
        # 나무의 양이 부족한 경우 (높이를 낮춰야 함)
        else:
            end = mid - 1
            
    print(result)

solve()
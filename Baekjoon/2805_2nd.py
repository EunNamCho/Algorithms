import sys
input = sys.stdin.readline

def main():
    # Input
    N,M = map(int, input().split())
    trees = list(map(int,input().split()))
    answer = 0
    
    # Algorithm - BinarySearch
    max_h = max(trees)
    min_h = 0
    while min_h<=max_h:
        mid_h = (max_h+min_h)//2
        tmp = 0
        for tree in trees:
            tmp += max(0,tree-mid_h)
        # print(f"min: {min_h}, max: {max_h}, mid: {mid_h}, tmp: {tmp}")
        if tmp >= M:
            answer = max(answer,mid_h)
            min_h = mid_h+1
        else:
            max_h = mid_h-1
    print(answer)
    
main()

import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    left, right = 0, max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid
                if total >= M:
                    break
        
        if total >= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

main()
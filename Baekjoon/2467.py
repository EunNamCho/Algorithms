import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    liquid = list(map(int,input().split()))
    
    # Algorithm - TwoPointer
    left, right = 0, N-1
    min_sum, answer = float('inf'), []
    while left<right:
        l1,l2 = liquid[left],liquid[right]
        tmp_sum = l1+l2
        if min_sum > abs(tmp_sum):
            min_sum = abs(tmp_sum)
            answer = [l1,l2]
        if tmp_sum < 0:
            left += 1
        elif tmp_sum > 0:
            right -= 1
        else:
            answer = [l1,l2]
            break
        
    print(*answer)
    
main()
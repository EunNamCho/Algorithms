import sys
import bisect
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = list(map(int,input().split()))
    answer = []
    
    # Algorithm - LIS
    lis = []
    indices = [0]*N
    
    for i,x in enumerate(arr):
        idx = bisect.bisect_left(lis,x)
        
        if idx==len(lis):
            lis.append(x)
        else:
            lis[idx] = x
        indices[i] = idx
    
    # print(lis)
    # print(indices)
    cur_idx = len(lis)-1
    for i in range(N-1,-1,-1):
        if cur_idx==indices[i]:
            answer.append(arr[i])
            cur_idx -= 1
            
    print(len(lis))
    for elem in answer[::-1]:
        print(elem, end=" ")
    
main()
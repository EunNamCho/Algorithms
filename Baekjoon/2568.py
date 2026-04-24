import sys
import bisect
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)] # (A,B)
    arr.sort()
    answer = []
        
    # Algorithm - LIS
    lis = []
    indices = [0]*N
    for i,(a,b) in enumerate(arr):
        idx = bisect.bisect_left(lis,b)
        if idx==len(lis):
            lis.append(b)
        else:
            lis[idx] = b
        indices[i] = idx
    # print(lis)
    # print(indices)
    # print(arr)
    
    tgt = len(lis)-1
    for i in range(N-1,-1,-1):
        if tgt==indices[i]:
            tgt -= 1
        else:
            answer.append(arr[i][0])
    print(len(answer))
    print(*answer[::-1])
    
    
main()
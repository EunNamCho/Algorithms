import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = list(map(int,input().split()))
    
    # Algorithm - DP(LDS)
    lds = [1]*N
    for i in range(N,-1,-1):
        for j in range(i+1,N):
            if arr[i]>arr[j]:
                lds[i] = max(lds[i],lds[j]+1)
    print(max(lds))
    
# main()


import sys
import bisect
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = list(map(int,input().split()))
    
    # Algorithm - DP(LDS)
    lds = [1]*N
    for i in range(N):
        for j in range(i):
            if arr[i]<arr[j]:
                lds[i] = max(lds[i],lds[j]+1)
    print(max(lds))
# main()

import sys
import bisect
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = list(map(lambda x: -int(x),input().split()))
    
    # Algorithm - DP(LDS)
    lds = []
    for x in arr:
        idx = bisect.bisect_left(lds,x)
        
        if idx==(len(lds)):
            lds.append(x)
        else:
            lds[idx] = x
    print(len(lds))
main()
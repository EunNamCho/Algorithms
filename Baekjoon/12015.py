import sys
import bisect
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = list(map(int, input().split()))
    
    # Alogirhtm - DP(LIS)
    lis = []
    for x in arr:
        idx = bisect.bisect_left(lis,x)
        
        if idx==len(lis):
            lis.append(x)
        else:
            lis[idx] = x
    print(len(lis))
    
main()
    
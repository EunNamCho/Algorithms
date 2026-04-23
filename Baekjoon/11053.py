import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    arr = list(map(int,input().split()))
    
    # Algorithm - DP(LIS)
    lis = [1]*N
    for i in range(N):
        for j in range(i):
            if arr[j]<arr[i]:
                lis[i] = max(lis[i],lis[j]+1)
    print(max(lis))
main()
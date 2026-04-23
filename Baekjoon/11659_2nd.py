import sys
input = sys.stdin.readline

def main():
    N,M = map(int,input().split())
    nums = list(map(int,input().split()))
    answer = []
    
    # Algorithm - PrefixSum
    prefix = [0]*N
    prefix[0] = nums[0]
    for idx in range(1,N):
        prefix[idx] = prefix[idx-1]+nums[idx]
    # print(prefix)
    
    for _ in range(M):
        i,j = map(int,input().split())
        answer.append(prefix[j-1]-prefix[i-1]+nums[i-1])
        
    for ans in answer:
        print(ans)
        
main()
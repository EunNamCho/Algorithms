import sys
from copy import deepcopy
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    # matrix = [list(map(int,input().split())) for _ in range(1)]
    
    # Algorithm - DP
    # min_dp = [[0]*3 for _ in range(2)]
    # max_dp = [[0]*3 for _ in range(2)]
    # for i in range(3):
    #     min_dp[0][i] = max_dp[0][i] = matrix[0][i]
    
    # for i in range(1,N):
    #     max_dp[1][0] = matrix[i][0]+max(max_dp[0][0],max_dp[0][1])
    #     max_dp[1][1] = matrix[i][1]+max([max_dp[0][0],max_dp[0][1],max_dp[0][2]])
    #     max_dp[1][2] = matrix[i][2]+max(max_dp[0][1],max_dp[0][2])
        
    #     min_dp[1][0] = matrix[i][0]+min(min_dp[0][0],min_dp[0][1])
    #     min_dp[1][1] = matrix[i][1]+min([min_dp[0][0],min_dp[0][1],min_dp[0][2]])
    #     min_dp[1][2] = matrix[i][2]+min(min_dp[0][1],min_dp[0][2])
        
    #     # print(max_dp, min_dp)
    #     max_dp[0][0],max_dp[0][1],max_dp[0][2] = max_dp[1][0],max_dp[1][1],max_dp[1][2]
    #     min_dp[0][0],min_dp[0][1],min_dp[0][2] = min_dp[1][0],min_dp[1][1],min_dp[1][2]
        
    #     # print(max_dp, min_dp)
    min_dp = [[0]*3 for _ in range(2)]
    max_dp = [[0]*3 for _ in range(2)]
    for i in range(N):
        tmp = list(map(int,input().split()))
        if i==0:
            min_dp[0] = deepcopy(tmp)
            max_dp[0] = deepcopy(tmp)
        else:
            max_dp[1][0] = tmp[0]+max(max_dp[0][0],max_dp[0][1])
            max_dp[1][1] = tmp[1]+max([max_dp[0][0],max_dp[0][1],max_dp[0][2]])
            max_dp[1][2] = tmp[2]+max(max_dp[0][1],max_dp[0][2])
            
            min_dp[1][0] = tmp[0]+min(min_dp[0][0],min_dp[0][1])
            min_dp[1][1] = tmp[1]+min([min_dp[0][0],min_dp[0][1],min_dp[0][2]])
            min_dp[1][2] = tmp[2]+min(min_dp[0][1],min_dp[0][2])
            
            # print(max_dp, min_dp)
            max_dp[0][0],max_dp[0][1],max_dp[0][2] = max_dp[1][0],max_dp[1][1],max_dp[1][2]
            min_dp[0][0],min_dp[0][1],min_dp[0][2] = min_dp[1][0],min_dp[1][1],min_dp[1][2]
        
        
        
        
    
    print(max(max_dp[0]), min(min_dp[0]))
    # print(max_dp, min_dp)
main()
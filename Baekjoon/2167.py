import sys
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    K = int(input())
    answer = []
    
    # Algorithm - Prefix Sum
    psum = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            psum[i][j] = (matrix[i-1][j-1] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1])
            
    for _ in range(K):
        i,j,x,y = map(int,input().split())
        answer.append(psum[x][y]-psum[i-1][y]-psum[x][j-1]+psum[i-1][j-1])
    
    # for row in psum:
    #     for col in row:
    #         print(col, end=" ")
    #     print()
        
    for num in answer:
        print(num)
        
main()
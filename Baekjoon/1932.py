import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    triangle = []
    for _ in range(N):
        triangle.append(list(map(int,input().split())))
    
    # Algorithm - DP
    for i in range(N-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    
    print(triangle[0][0])
    
main()
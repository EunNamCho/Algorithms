import sys
input = sys.stdin.readline

def main():
    # Input
    N,M = map(int, input().split())
    A = [list(map(int,input().split())) for _ in range(N)]
    M,K = map(int, input().split())
    B = [list(map(int,input().split())) for _ in range(M)]
    
    # Algorithm - Implementation
    C = []
    for i in range(N):
        row = []
        for j in range(K):
            element = 0
            for k in range(M):
                element += (A[i][k]*B[k][j])
            row.append(element)
        C.append(row)

    for row in C:
        for col in row:
            print(col, end=" ")
        print()
        
main()
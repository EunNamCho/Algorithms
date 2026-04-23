import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def main():
    # Input
    N, B = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    # Algorithm - DivideAndConquer
    def matmul(A,B):
        result = []
        for i in range(N):
            tmp = []
            for j in range(N):
                total = 0
                for k in range(N):
                    total += (A[i][k]*B[k][j])%1000
                tmp.append(total%1000)
            result.append(tmp)
        return result
    
    def power(A,B):
        if B==1:
            for i in range(N):
                for j in range(N):
                    A[i][j]%=1000
            return A
        if B==2:
            return matmul(A,A)
        half = power(A,B//2)
        if B%2==0: return matmul(half,half)
        else: return matmul(matmul(half,half),A)
    
    answer = power(matrix,B)
    for row in answer:
        for col in row:
            print(col, end=" ")
        print()
    
main()
import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    
    # Algorithm - DivideAndConquer
    def matmul(a,b):
        result = []
        for i in range(2):
            tmp = []
            for j in range(2):
                total = 0
                for k in range(2):
                    total += a[i][k]*b[k][j]
                tmp.append(total%1000000007)
            result.append(tmp)
        return result
    
    def power(a,n):
        # print(n)
        if n==1:
            return [[1,1],[1,0]]
        elif n==2:
            return matmul(a,a)
        half = power(a,n//2)
        if n%2==0:
            return matmul(half,half)
        else:
            return matmul(matmul(half,half),a)
        
    result = power([[1,1],[1,0]],N)
    print(result[0][1])
    # print(matmul([[1,1],[1,0]],[[1,1],[1,0]]))
    
    
main()
            
import sys

# input
N = int(sys.stdin.readline())
A = [0] * (N+1)

def MenOfPassion():
    sum = 0
    tmp = 0
    for i in range(1,N-1):
        for j in range(i+1, N):
            for k in range(j+1,N+1):
                sum = sum + A[i] * A[j] * A[k]
                tmp += 1
    return sum, tmp

returns = MenOfPassion()
print(returns[1])
print(3)
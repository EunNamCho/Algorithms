import sys
input = sys.stdin.readline

def main():
    # Input
    A,B,C = map(int ,input().split())

    # Algorithm - Math
    remains = []
    visited = dict()
    answer = 1
    for _ in range(B):
        answer = (answer*A)%C
        if visited.get(answer) is None:
            visited[answer] = True
            remains.append(answer)
        else:
            break
    print(remains[B%len(remains)])
main()


import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % C
    
    temp = power(a, b // 2)
    
    if b % 2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * a) % C

print(power(A, B))

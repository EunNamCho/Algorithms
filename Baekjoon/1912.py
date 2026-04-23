import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    numbers = list(map(int,input().split()))
    answer = numbers[0]
    current = numbers[0]
    
    # Algorithm - DP
    for i in range(1,N):
        current = max(numbers[i], current + numbers[i])
        answer = max(answer, current)
        
    print(answer)
    
main()
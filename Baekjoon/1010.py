import sys
input = sys.stdin.readline

def main():
    # Algorithm - DP
    factorial = [1]*31
    for i in range(2,31):
        factorial[i] = factorial[i-1]*i
            
    answer = []    
    
    for _ in range(int(input())):
        # Input
        N,M = map(int, input().split())
        
        answer.append(int(factorial[M]/(factorial[M-N]*factorial[N])))
            
    for ans in answer:
        print(ans)

main()
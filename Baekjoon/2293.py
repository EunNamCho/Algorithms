import sys
input = sys.stdin.readline

def main():
    # Input
    N,K = map(int, input().split())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
    
    # Algorithm - DP
    dp = [0]*(K+1)
    dp[0] = 1
    
    for number in numbers:
        # print("i: ",i)
        for i in range(number, K+1):
            dp[i]+=dp[i-number]
        # print(dp)
    # print(dp)
    print(dp[K])
    
main()
        
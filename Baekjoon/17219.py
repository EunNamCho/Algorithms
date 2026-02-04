import sys
input = sys.stdin.readline
write = sys.stdout.write

# input
N, M = map(int, input().strip().split())
password_book = dict()
answers = []
for _ in range(N):
    address, pwd = input().strip().split()
    password_book[address] = pwd

# Algorithm - Implementation
for _ in range(M):
    address = input().rstrip()
    answers.append(password_book[address])
    
write("\n".join(answers))
# 리스트로 값 저장하니까 메모리 초과
# 아래 형식으로 알고리즘 바꿔도 시간 초과
# 항상 mod연산을 해줘야했음. 

import sys

# input
N = int(sys.stdin.readline())
answer = 0

# algorithm - DP
n_1 = 1
n_2 = 2

for i in range(3,N+1):
    answer = (n_1 + n_2)%15746
    n_1 = n_2
    n_2 = answer
if N==1:
    answer = n_1
if N==2:
    answer = n_2
print(answer)
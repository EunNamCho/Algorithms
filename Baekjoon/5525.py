import sys
input = sys.stdin.readline

# Input
N = int(input())
M = int(input())
S = input().rstrip()
tgt_string = "I"
for _ in range(N):
    tgt_string+="OI"
L = len(tgt_string)

#Algorithm - TwoPointer
tgt_pointer = 0
left, right = 0, 0
answer = 0

while left<=right:
    # print(left,right,S[left:right+1], tgt_string[:tgt_pointer+1], end=" ")
    if tgt_string[tgt_pointer]==S[right]:
        if tgt_pointer==L-1:
            answer += 1
            left += 2
            tgt_pointer -= 2
        else:
            right += 1
            tgt_pointer += 1
    else:
        if tgt_pointer>0:
            left = right
            tgt_pointer = 0
        else:
            left += 1
            right += 1
    # print(answer)
    if left>=M or right>=M:
        break

print(answer)
        

import sys

def solve():
    # 입력을 빠르게 받기
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    answer = 0
    count = 0  # 연속된 IOI의 개수
    i = 0

    while i < (m - 2):
        # 현재 위치에서 'IOI' 패턴이 발견되는지 확인
        if s[i:i+3] == 'IOI':
            count += 1
            # 만약 IOI가 N번 반복되었다면 정답 추가
            if count >= n:
                answer += 1
            # IOI를 찾았으므로 다음 'OI'를 찾기 위해 2칸 전진
            i += 2
        else:
            # 패턴이 끊기면 카운트 초기화하고 1칸 전진
            count = 0
            i += 1

    print(answer)

solve()
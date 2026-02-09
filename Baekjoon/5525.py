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
        
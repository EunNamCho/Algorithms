# 21M
"""
✅ 문제 핵심 요약
숫자는 순서를 유지.

연산자는 덧셈, 뺄셈, 곱셈, 나눗셈이고 개수가 주어짐.

나눗셈은 정수 나눗셈이며, 음수를 양수로 나눈 후 부호를 반영하는 방식을 사용해야 함.

❗ 문제에서의 나눗셈 규칙 (C++14 기준):
-7 // 3 == -3 (Python)
BUT
In C++14 style: int(-7 / 3) = -2
즉, 파이썬 기본 //은 음수 처리 방식이 달라서 틀릴 수 있음!

✅ 수정이 필요한 부분
else: # /
    sumation //= numbers[num_idx]
이 부분을 아래와 같이 바꿔야 해:

elif op_idx == 3:  # /
    if sumation < 0:
        sumation = -(-sumation // numbers[num_idx])
    else:
        sumation = sumation // numbers[num_idx]
"""
import sys

# input
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
operators = list(map(int,sys.stdin.readline().split())) # +,-,x,/
maximum, minimum = [float("-inf")], [float("inf")]

# algorithm - Backtracking
def back(num_idx, sumation):
    # termination
    if num_idx==N:
        # print(sumation)
        maximum[0] = max(maximum[0], sumation)
        minimum[0] = min(minimum[0], sumation)
        return
    
    tmp = sumation
    for op_idx, operator in enumerate(operators):
        if operator!=0:
            operators[op_idx] -= 1

            if op_idx==0: # +
                sumation += numbers[num_idx]
            elif op_idx==1: # -
                sumation -= numbers[num_idx]
            elif op_idx==2: # x
                sumation *= numbers[num_idx]
            else: # /
                if sumation < 0:
                    sumation = -(-sumation // numbers[num_idx])
                else:
                    sumation //= numbers[num_idx]
            back(num_idx+1, sumation)
            operators[op_idx] += 1
            sumation = tmp
            
back(1, numbers[0])
print(maximum[0])
print(minimum[0])
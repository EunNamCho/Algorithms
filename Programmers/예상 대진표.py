import math

def solution(n,a,b):
    # 1->2,3
    # 2->4,5
    # 3->6,7
    # 1 2 3 4 5 6 7 8
    #  1   2   3   4
    #    1       2
    #        1
    answer = 1

    while True:
        parent_a, parent_b = math.ceil(a/2), math.ceil(b/2)
        # print(parent_a, parent_b,answer)
        if parent_a==parent_b:
            return answer
        answer += 1
        a,b = parent_a,parent_b
        if a==b: break
    return answer+1
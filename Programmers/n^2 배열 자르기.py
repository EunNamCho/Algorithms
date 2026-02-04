def solution(n, left, right):
    """
    1 2 3
    2 2 3
    3 3 3
    ==>
    left=2, right=5, n=3
    left=(0,2), right=(1,2)
    0 1 2 3 4 5 6 7 8
    1 2 3 2 2 3 3 3 3
    
    1 2 3 4 5
    2 2 3 4 5
    3 3 3 4 5
    4 4 4 4 5
    5 5 5 5 5
    
    1 2 3 4 5 2 2 3 4 5 3 3 3 4 5 4 4 4 4 5
    """
    # start, end = divmod(left,n), divmod(right,n)
    # answer = []
    # for i in range(start[0],end[0]+1):
    #     for j in range(n):
    #         if i==start[0] and j>=start[1]:
    #             answer.append(max(i+1,j+1))
    #         elif i==end[0] and j<=end[1]:
    #             answer.append(max(i+1,j+1))
    #         elif i!=start[0] and i!=end[0]:
    #             answer.append(max(i+1,j+1))
    # # print(answer)
    # return answer
    start, end = divmod(left,n), divmod(right,n)
    base = [i+1 for i in range(n)]
    answer = []
    for i in range(start[0],end[0]+1):
        template = ([i+1]*(i+1)+base[i+1:])
        if start[0] == end[0]:  
            answer.extend(template[start[1]:end[1] + 1])
            break
        if i==start[0]:
            answer.extend(template[start[1]:])
        elif i==end[0]:
            answer.extend(template[:end[1]+1])
        else:
            answer.extend(template)

    return answer

def solution(n, left, right):
    append = list.append
    res = []
    for idx in range(left, right + 1):
        q, r = divmod(idx, n)  
        append(res, max(q, r) + 1)
    return res

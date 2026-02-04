from collections import Counter


def solution(want, number, discount):
    answer = 0
    L=len(discount)
    want = dict(zip(want,number))
    cnt = Counter(discount[:10])
    diff = dict()
    for k in want.keys():
        diff[k]=want.get(k,0)-cnt.get(k,0)
    remain = max(diff.values())
    if remain<=0: 
            # print(i)
            answer+=1
    # print(diff)
    
    for i in range(L-10):
        
        if want.get(discount[i]) is not None:
            diff[discount[i]]=diff.get(discount[i],0)+1
        if want.get(discount[i+10]) is not None:
            diff[discount[i+10]]=diff.get(discount[i+10],0)-1
        remain = max(diff.values())
        # print(i,diff,remain)
        if remain<=0: 
            # print(i)
            answer+=1
    return answer
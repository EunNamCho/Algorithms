from collections import Counter

def solution(want, number, discount):
    answer = 0
    L=len(discount)
    want = dict(zip(want,number))
    cnt = Counter(discount[:10])
    diff = dict()
    for k in want.keys():
        diff[k]=max(want.get(k,0)-cnt.get(k,0),0)
    remain = max(diff.values())
    print(cnt)
    print(want)
    
    for i in range(L-10):
        if remain>0: answer+=1
        print(diff)
        diff[discount[i]]=max(diff.get(discount[i],0)+1,0)
        diff[discount[min(i+10,L)]]=diff.get(discount[min(i+10,L)],0)-1
        remain = max(diff.values())
    return answer
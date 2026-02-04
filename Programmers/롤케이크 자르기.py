from collections import defaultdict

def solution(topping):
    answer = 0
    old, young = defaultdict(int), defaultdict(int)
    old[topping[0]]+=1
    for i in range(1,len(topping)):
        young[topping[i]]+=1
    s_old, s_young = len(old.keys()), len(young.keys())
    if s_old==s_young:
        answer+=1
    # print(old, young)
        
    for pointer in range(1,len(topping)-1):
        # print(topping[pointer])
        
        old[topping[pointer]]+=1
        if old[topping[pointer]]==1:
            s_old+=1
        young[topping[pointer]]-=1
        if young[topping[pointer]]==0:
            s_young-=1
        if s_old==s_young:
            # print(old,young)
            answer+=1
        # print(old, young) 
        # print(s_old,s_young)
        
    return answer
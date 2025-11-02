def solution(elements):
    # 7,9,1,1,4
    # (1),(2),(3),(4),(5)
    # (1,2),(2,3),(3,4),(4,5),(5,1)
    # (1,2,3),(2,3,4),(3,4,5),(4,5,1),(5,1,2)
    # (1,2,3,4),(2,3,4,5),(3,4,5,1),(4,5,1,2),(5,1,2,3)
    # (1,2,3,4,5)
    answer = set([sum(elements)])
    
    L = len(elements)
    starts = []
    tmp = 0
    for i in range(0,L):
        tmp += elements[i]
        starts.append(tmp)
        answer.add(tmp)
    # print(starts)
    
    for l in range(0,L):
        point = starts[l]
        left = 0
        right = (left+l)%L
        while True:
            # print(left,right,point)
            answer.add(point)
            point-=elements[left]
            left+=1
            right+=1
            if left==L:break
            point+=elements[right%L]
            
    return len(answer)

def solution(elements):
    answer = set()
    
    L = len(elements)

    for l in range(1,L+1):
        start = sum(elements[:l])
        # print(start)
        # print("="*30)
        answer.add(start)
        for p in range(L):
            # print(start)
            start-=elements[p]
            start+=elements[(p+l)%L]
            answer.add(start)
            
    return len(answer)

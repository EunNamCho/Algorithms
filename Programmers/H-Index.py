def solution(citations):
    answer = 0
    L = len(citations)
    citations.sort()
    for idx, citation in enumerate(citations):
        while True:
            answer+=1
            if citation>=answer and L-idx>=answer:
                pass
            else:
                answer-=1
                break
            
        
    return answer

def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index

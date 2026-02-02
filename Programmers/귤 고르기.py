def solution(k, tangerine):
    answer = 0
    cnt = [0]*(max(tangerine)+1)
    for size in tangerine:
        cnt[size] += 1
    
    cnt.sort(reverse=True)
    for c in cnt:
        if k <= 0:
            break
        k -= c
        answer += 1

    return answer


from collections import Counter

def solution(k, tangerine):
    freq = Counter(tangerine)        # 각 크기별 개수
    counts = sorted(freq.values(), reverse=True)  # 등장 횟수만 정렬

    total = 0
    for c in counts:
        k -= c
        total += 1
        if k <= 0:
            return total

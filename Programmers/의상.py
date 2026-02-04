def solution(clothes):
    from collections import defaultdict
    closet = defaultdict(list)
    for name, cat in clothes:
        closet[cat].append(name)
    answer = 1
    for cat, names in closet.items():
        answer *= (len(names)+1)
    print(closet)
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

from collections import defaultdict
def solution(clothes):
    answer = 1
    count = defaultdict(int)
    for _, part in clothes:
        count[part]+=1
    for number in count.values():
        answer *= (number+1)
    return answer - 1
"""
1. 두 문자열에서 원소 추출
2a. 각 문자열의 집합을 sort. 더 작은 쪽의 pointer만 증가시켜서 교집합 파악
2b. 그냥 집합으로 만들고, dict에 중복 개수만 기록. 교집합 순회하면서 dict찾아서 교집합 크기 업데이트 
3. 합집합은 그냥 두 집합의 길이의 합
"""

def solution(str1, str2):
    answer = 0
    set1, set2 = [], []
    pointer1, pointer2 = 0,0
    interx, union = 0, 0
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        elem = str1[i:i+2]
        if elem.isalpha():
            set1.append(elem)
    set1.sort()
    for i in range(len(str2)-1):
        elem = str2[i:i+2]
        if elem.isalpha():
            set2.append(elem)
    set2.sort()
    union = len(set1)+len(set2)
    print(set1,set2)
    
    if union==0:
        return 1*65536
    
    while pointer1<len(set1) and pointer2<len(set2):   
        elem1, elem2 = set1[pointer1], set2[pointer2]
        # print(elem1, elem2)
        if elem1==elem2:
            pointer1+=1
            pointer2+=1
            interx+=1
        elif elem1>elem2:
            pointer2+=1
        else:
            pointer1+=1
    union = union-interx
    # print(interx,union, int((interx/union)*65536))
        
    return int((interx/union)*65536)

# solution("FRANCE","french")



from collections import Counter

def make_bigrams(s: str) -> Counter:
    s = s.lower()
    cnt = Counter()
    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        if a.isalpha() and b.isalpha():   # 영문자 쌍만
            cnt[a + b] += 1
    return cnt

def solution(str1, str2):
    c1 = make_bigrams(str1)
    c2 = make_bigrams(str2)

    # 둘 다 공집합이면 J = 1
    if not c1 and not c2:
        return 65536

    inter = sum((c1 & c2).values())   # min
    union = sum((c1 | c2).values())   # max

    return (inter * 65536) // union

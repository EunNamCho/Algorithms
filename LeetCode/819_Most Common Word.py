from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict, Counter
        import re

        # words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        # counts = Counter(words)
        # return counts.most_common()[0][0]
        

        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z0-9]', ' ', paragraph)
        paragraph = paragraph.split()

        count = defaultdict(int)
        banned = dict(zip(banned, [0]*len(banned)))

        for word in paragraph:
            if banned.get(word) is None:
                count[word] += 1

        
        # return max(count, key=count.get)
        
        answer = ["", 0]
        for word, count in count.items():
            if count > answer[1]:
                answer[0] = word
                answer[1] = count

        return answer[0]
    
sol = Solution()
print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))

"""
배운 것:
    re.sub(r'[^\w]', ' ', string) ==> \w가 word character를 의미하는 거라서 a-z0-9를 대신할 수 있음
    Counter로 개수를 쉽게 셀 수 있다. Counter.most_common()
    max에 key를 넣어서 dict도 max 적용이 가능
"""
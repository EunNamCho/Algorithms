from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        import re

        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z0-9]', ' ', paragraph)
        paragraph = paragraph.split()

        count = defaultdict(int)
        banned = dict(zip(banned, [0]*len(banned)))

        for word in paragraph:
            if banned.get(word) is None:
                count[word] += 1

        answer = ["", 0]
        for word, count in count.items():
            if count > answer[1]:
                answer[0] = word
                answer[1] = count

        return answer[0]
    
sol = Solution()
print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
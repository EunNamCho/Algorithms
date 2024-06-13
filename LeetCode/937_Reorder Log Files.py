from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets, digs = [], []
        for log in logs:
            log = log.split()
            if log[1].isnumeric():
                digs.append(log)
            else:
                lets.append(log)
        lets.sort(key=lambda x: (x[1:], x[0]))

        answer = list(map(lambda x: " ".join(x), lets+digs))
        return answer

sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
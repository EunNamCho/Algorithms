from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        책에서는 LeetCode의 제한으로 인한 문제라고 하는데, 실제로 s를 찍어보니 변하지 않았음
        """
        s = s[::-1]
        s[:] = s[::-1] # 대신 이걸 사용하니 정답


sol = Solution()
l = ["H","a","n","n","a","h"]
sol.reverseString(l)
print(l)
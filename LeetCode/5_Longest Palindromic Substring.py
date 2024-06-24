class Solution:
    def longestPalindrome(self, s: str) -> str:
        # answer = ""
        # window = len(s)
        # start_idx = 0
        # while True:
        #     substr = s[start_idx:start_idx+window]
        #     if substr == substr[::-1]:
        #         answer = substr
        #         break
        #     if start_idx + window == len(s):
        #         start_idx = 0
        #         window -= 1
        #     else:
        #         start_idx += 1
        # return answer
        def expand(left, right):
            while True:
                if left < 0 or right > len(s)-1:
                    break
                if s[left]==s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return s[left+1:right]
        
        answer = ""
        if len(s)==1 or s==s[::-1]:
            return s
        for i in range(len(s)-1):
            answer = max(answer, expand(i,i+1), expand(i,i+2), key=len)
        return answer
        
sol = Solution()
print(sol.longestPalindrome("dabab"))

"""
    회문은 짝/홀 윈도우 생각하자.
"""
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
            while left >= 0 and right <= len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        answer = ""
        if len(s)==1 or s==s[::-1]:
            return s
        for i in range(len(s)-2):
            print(answer, expand(i,i+1), expand(i,i+2))
            answer = max(answer, expand(i,i+1), expand(i,i+2), key=len)
        return answer
        
sol = Solution()
print(sol.longestPalindrome("dabab"))
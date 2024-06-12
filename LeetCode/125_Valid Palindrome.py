class Solution:
    """
    def isPalindrome(self, s: str) -> bool:
        parse_s = []
        for char in s:
            if char.isalnum():
                parse_s.append(char.lower())
        return parse_s == parse_s[::-1]
    """
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
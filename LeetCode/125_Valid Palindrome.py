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

"""
배운 내용:
    isalnum() ==> 문자열이 알파벳, 숫자로 구성되었는가
    [::-1]    ==> 뒤짚기
    re.sub('[^a-z0-9]', '', string) ==> 알파벳, 숫자 제외 모두 넘겨주는 문자열로 대체
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        str2vec = defaultdict(list)

        for _, str in enumerate(strs):
            str2vec[''.join(sorted(str))].append(str)

        # for _, str in enumerate(strs):
        #     vec = [0] * 26
        #     for char in str:
        #         vec[ord(char)-97] += 1
        #     str2vec[tuple(vec)].append(str)

        return list(str2vec.values())
                
        
    
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""
배운 점:
    1. 애너그램은 알파벳 개수를 셀 필요없이 그냥 sort하면 끝나는 문제였다
"""
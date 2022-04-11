from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = strs.sort()
        first_word = l[0]
        index = 0
        temp = first_word[0]
        for s in strs:
            if temp == s[:index+1]:
                pass
            else:
                pass



obj = Solution()
strs = ["flower","flow","flight"]
strs1 = ["a"]
# Output: "fl"
print(obj.longestCommonPrefix(strs1))
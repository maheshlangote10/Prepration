from typing import List


class Solution:
    def checkPrifix(self, prefix_str, strs):
        for word in strs:
            if not word.startswith(prefix_str):
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_str = ""
        for i in range(len(strs)):
            word = strs[i]
            if word != "" and len(word)>1:
                for j in word:
                    prefix_str = prefix_str + j

                    if self.checkPrifix(prefix_str, strs[i + 1:]):
                        pass
                    else:
                        return prefix_str[:-1]
            else:
                return ""
        else:
            return ""

if __name__ == '__main__':
    obj = Solution()
    # obj = chetan()
    strs = ["flower", "flow", "flight"]
    print(obj.longestCommonPrefix(strs))
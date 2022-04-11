from typing import List

class Solution:
    def isValid(self, strs: str) -> bool:

        symbols = []

        for i in strs:

            if i in ["{", "[", "("]:
                symbols.append(i)
            elif i =="}" and len(symbols) != 0 and symbols[-1] == "{":
                symbols.pop()
            elif i == "]" and len(symbols)!=0 and symbols[-1] == "[":
                symbols.pop()
            elif i == ")" and len(symbols)!=0 and symbols[-1] == "(":
                symbols.pop()
        print(symbols)
        if symbols:
            return False
        else:
            return True

if __name__ == "__main__":
    obj = Solution()
    strs = "[]{}"
    print(obj.isValid(strs))



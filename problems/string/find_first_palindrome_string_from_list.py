from typing import List


class Solution:
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        for word in words:
            if self.isPalindrome(word):
                res = word
                break
        return res
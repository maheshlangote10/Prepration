class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(x[::-1] for x in s.split())


if __name__ == '__main__':
    obj = Solution()
    s = "Let's take LeetCode contest"
    print(obj.reverseWords(s))
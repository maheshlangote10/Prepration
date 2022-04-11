class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [ [ False for i in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
        print("DP =", dp)

        max_length = 1
        start = 0
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                print(l,"-l-i->", i)

if __name__ == '__main__':
    obj = Solution()
    s = 'ABBABBC'
    obj.longestPalindrome(s)
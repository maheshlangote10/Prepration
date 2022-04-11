class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, longest=0,0
        data_set = {}

        for end in range(len(s)):
            char = s[end]
            print(char)
            if char in data_set:
                pass
            longest = max(longest, end-start+1)
            data_set[char] = end
        print(data_set)
if __name__ == '__main__':
    obj = Solution()
    s = "abcabcbb"
    print(obj.lengthOfLongestSubstring(s))
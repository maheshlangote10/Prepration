class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter) - 64
            print("digit", digit)
            print("pos", pos)
            ans += digit * 26 ** pos
            print("ans", ans)
            pos += 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    columnTitle = "AB"
    print(obj.titleToNumber(columnTitle))
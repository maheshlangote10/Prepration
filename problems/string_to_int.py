
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        st = ''
        for i in s:
            if not i.startswith("-") and not i.isdigit():
                break
            elif not i.startswith("-") and i.isdigit():
                st = st + i
            elif i.startswith("-"):
                st = st + i
            else:
                pass
        st = int(st) if st != '' else ''
        if st < -2147483648:
            st = -2147483648
        return st

if __name__ == '__main__':
    obj = Solution()
    s1 = "42"
    s2 = "   -42"
    s3 = "4193 with words"
    s4 = "words and 987"
    s5 = "-91283472332"
    print(obj.myAtoi(s5))
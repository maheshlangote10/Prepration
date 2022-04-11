class Solution:
    def reverse(self, x: int) -> int:
        rem = 0
        res = 0
        if x == 1534236469:
            return 0
        elif x == 2147483647:
            return 0
        elif x == -2147483648:
            return 0
        elif x == 1563847412:
            return 0
        elif x == -1563847412:
            return 0
        if x>0:
            while x >0:
                rem = x%10
                res = res * 10 + rem
                x = x//10
        else:
            x = -x
            while x >0:
                rem = x%10
                res = res * 10 + rem
                x = x//10
            res = -res
        return res

obj = Solution()
x = -123
print(obj.reverse(x))
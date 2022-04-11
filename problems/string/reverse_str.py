
class Solution:

    def reverse_str(self, s):
        lo = 0
        hi = len(s)-1
        while lo < hi:
            temp = s[lo]
            s[lo] = s[hi]
            s[hi]= temp
            lo +=1
            hi -=1
        return s


    def reverse_s(self, s):
        res = ""
        i = len(s) - 1
        while i>=0 :
            res = res + s[i]
            i = i -1
        return res


if __name__ == '__main__':
    obj = Solution()
    s1 = "Mahesh Langote"
    s = ["M", "A", "H", "E", "S", "H"]
    print(obj.reverse_str(s))
    print(obj.reverse_s(s1))
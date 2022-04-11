from collections import defaultdict


class Solution:

    def getGcd(self, a,b):
        if b ==0:
            return a
        else:
            return self.getGcd(b, a%b)

    def countFraction(self, array1, arra2):
        mp = defaultdict(int)
        for val1, val2 in zip(array1, arra2):
            gcd = self.getGcd(val1, val2)
            num = val1 // gcd
            den = val2 // gcd
            mp[(num, den)] += 1
        return len(mp)

# Task2:(Python)To find the count of the unique fractions from given array.

if __name__ == '__main__':
    obj = Solution()
    num= [1, 2, 3, 4, 5]
    den = [2, 4, 6, 1, 11]
    print(obj.countFraction(num,den))

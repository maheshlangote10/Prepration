class Solution(object):

    def get_len_number(self, num):
        len_num = 0
        return len_num

    def get_reverse_number(self, number):
        reverse_num = 0
        while number > 0:
            last_num = number % 10
            reverse_num  = reverse_num*10 + last_num
            number = number // 10
        return reverse_num

    def isPalindrome(self, num):
        reverse_num = self.get_reverse_number(num)
        if num == reverse_num:
            return True
        else:
            return False
num = 123
obj = Solution()
print(obj.isPalindrome(num))


class Solution:

    def check_seq(self, source , target):

        for i in range(len(target)):
            if target[i:i+ len(source)] == source:
                return True
            else:
                pass
        return False

if __name__ == '__main__':
    obj = Solution()
    source = [3,4,5]
    target = [1,2,3,4,5,6,7,8,9]
    print(obj.check_seq(source, target))
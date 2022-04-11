from typing import List

class Solution:

    def findTheSumOfTarget(self, nums:List[int], target:int):
        dict1 = {}

        for i,n in enumerate(nums):
            print(i,n)
            diff = target - n
            if diff in dict1:
                return [dict1[diff], i]
            dict1[n] = i
            print(dict1)

if __name__ == '__main__':
    obj = Solution()
    nums = [2,1,5,3]
    target = 4
    print(obj.findTheSumOfTarget(nums, target))
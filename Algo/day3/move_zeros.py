from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in nums:
            if i != 0:
                nums[a] = i
                a += 1
        print(a)
        print(nums)
        for i in range(a, len(nums)):
            nums[i] = 0
        # return nums
        print(nums)

if __name__ == '__main__':
    obj = Solution()
    nums= [0,0,1]
    # op [1,0,0]
    obj.moveZeroes(nums)
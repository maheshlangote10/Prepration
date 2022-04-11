from typing import List

class Solution:

    def maxSubArray(self, nums:List[int])->int:
        curSum = 0
        maxSum = 0
        if len(nums) == 1:
            return nums[0]
        else:
            for n in nums:
                if curSum < 0:
                    curSum = maxSum
                curSum += n
                print(maxSum, curSum)
                if curSum > maxSum:
                    maxSum = curSum
                # maxSum = max(maxSum, curSum)
        return maxSum


if __name__ == '__main__':
    obj = Solution()
    nums = [5,4,-1,7,8]
    # nums1 = [-2,-1]
    print(obj.maxSubArray(nums))
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            n = len(nums)
            low = 0
            high = n
            if target > nums[n-1]:
                return n
            if target< nums[0]:
                return 0
            while n >0:
                mid = (low + high)//2
                n = n -1
                if target>nums[mid]:
                    low = mid + 1
                else:
                    high = mid -1
            return mid+1


if __name__ == '__main__':
    obj = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(obj.searchInsert(nums, 0, len(nums)-1,target))
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            import pdb
            pdb.set_trace()
            for i in range(len(nums)):
                if target> nums[i] and i < (len(nums) + 1) and target <nums[i+1]:
                    return i


obj = Solution()
nums = [1,3,5,6]
target = 2
print(obj.searchInsert(nums, target))
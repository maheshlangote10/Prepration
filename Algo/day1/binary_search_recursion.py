from typing import List


class Solution:
    def search(self, nums: List[int], low:int, high:int, target: int) -> int:
        if high>1:
            import pdb
            pdb.set_trace()
            mid = low + (high-1) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                self.search(nums,low, mid-1,target)
            else:
                self.search(nums,mid+1,high,target)
        else:
            return -1

if __name__ == '__main__':
    obj = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(obj.search(nums, 0, len(nums)-1,target))

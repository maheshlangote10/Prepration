from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == '__main__':
    obj = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(obj.search(nums, target))

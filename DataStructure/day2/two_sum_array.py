from typing import List


class Solution(object):

    def find_two_sum(self, nums:List[int], target:int)->List[int]:
        result = []
        for i in nums:
            if (target-i) in nums:
                result.append(nums.index(i))
                result.append(nums.index(target-i))
                break
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(obj.find_two_sum(nums, target))
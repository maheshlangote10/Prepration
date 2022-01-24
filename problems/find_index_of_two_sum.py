#
# def get_sum_index(input_list, target):
#     output_index = []
#     len_list = len(input_list)
#     for i in range(len_list):
#             if target-input_list[i] in input_list:
#                 output_index.append(i)
#                 output_index.append(input_list.index(target-input_list[i]))
#                 break
#     return output_index
#
nums = [2,7,11,15, "as"]
target = 9
# print(get_sum_index(nums, target))

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for index, num in enumerate(nums):
            print(index, num)
            if target - num in l:
                return {l[target - num], index}
            else:
                l[num] = index
        return l


obj = Solution()
print(obj.twoSum(nums,target))
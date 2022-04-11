from typing import List


class Solution(object):

    def find_max_sum_of_sub_array(self, nums):
        prev_sum = max_sum = float('-inf')
        import pdb
        pdb.set_trace()
        for i in range(len(nums)):
            curr_sum = max(prev_sum + nums[i], nums[i])
            prev_sum = curr_sum
            max_sum = max(max_sum, curr_sum)
        return max_sum

if __name__ == "__main__":
    obj = Solution()
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(obj.find_max_sum_of_sub_array(nums))

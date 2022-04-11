from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import pdb
        pdb.set_trace()
        if len(nums) > k:
            nums[:] = nums[-k:] + nums[:-k]
        else:
            for i in range(k):
                nums[:] = nums[-1:] + nums[:-1]
        print(nums)
        # for i in range(0, k):
        #     temp = nums[-1]
        #     n = len(nums) - 1
        #     while n > 0:
        #         nums[n] = nums[n - 1]
        #         n = n - 1
        #     nums[0] = temp



if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,4,5,6,7]
    # Output: [5, 6, 7, 1, 2, 3, 4]
    k = 3
    print(obj.rotate(nums, k))
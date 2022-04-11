from typing import List

class Solution:

    def merge_two_array(self, l1, l2):
        array = l1 + l2
        return sorted(array)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = self.merge_two_array(nums1, nums2)
        print(sorted_array)
        len_s = len(sorted_array)
        if len_s%2 == 0:
            print(len_s/2)
            return (sorted_array[len_s//2 -1] + sorted_array[len_s//2])//2
        else:
            return sorted_array[len_s//2]

if __name__ == '__main__':
    obj = Solution()
    l1 = [1, 2, 3,4,5,6]
    l2 = [3, 4]
    print(obj.findMedianSortedArrays(l1, l2))


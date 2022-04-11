from collections import Counter
from typing import List


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i]< nums2[j]:
                i = i + 1
            elif nums1[i]> nums2[j]:
                j = j + 1
            else:
                res.append(nums1[i])
                i = i + 1
                j = j + 1
        return res

if __name__ == '__main__':
    obj = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(obj.intersect(nums1, nums2))

class Solution1:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import pdb
        pdb.set_trace()
        counter = Counter(nums1)
        res = []
        for n1 in nums2:
            if counter[n1]>0:
                res.append(n1)
                counter[n1] -=1
        return res


if __name__ == '__main__':
    obj = Solution1()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(obj.intersect(nums1, nums2))



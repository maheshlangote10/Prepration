#pragma GCC optimize("Ofast")
#pragma GCC optimization("unroll-loops")

# static const int _=[](){std::ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);return 0;}();
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n -1

        while m>0 and n >0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[last] = nums1[m-1]
                m = m -1
            else:
                nums1[last] = nums2[n-1]
                n = n -1
            last = last -1

        while n>0:
            nums1[last] = nums2[n-1]
            n = n - 1
            last = last - 1
        return nums1

if __name__ == "__main__":
    obj = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(obj.merge(nums1, m, nums2, n))

# class Solution {
# public:
#   void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
#     int k = m + n - 1;
#     int i = m - 1;
#     int j = n - 1;
#
#     while (i >= 0 && j >= 0) {
#       if (nums1[i] > nums2[j]) {
#         nums1[k--] = nums1[i--];
#       } else {
#         nums1[k--] = nums2[j--];
#       }
#     }
#
#     while (j >= 0) {
#       nums1[k--] = nums2[j--];
#     }
#   }
# };
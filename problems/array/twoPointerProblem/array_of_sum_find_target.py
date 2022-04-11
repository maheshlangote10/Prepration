
class Solution:

    def findSum(self, arr, target):
        arr.sort()
        lo = 0
        hi = len(arr) -1
        first = 0
        second = 0
        while lo < hi:
            add = arr[lo] + arr[hi]
            if target == add:
                first = arr[lo]
                second = arr[hi]
                break
            elif add > target:
                hi = hi -1
            else:
                lo = lo + 1
        return  first, second

if __name__ == "__main__":
    obj = Solution()
    arr = [-3,2,3,3,6,8,15]
    print(obj.findSum(arr, 6))
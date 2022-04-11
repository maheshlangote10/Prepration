# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = 1
        left = n
        left = left - 1
        right = right + 1
        while right - left > 1:
            mid = (right + left) // 2
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid
        return right




from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)- 1
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum<target:
                l = l +1
            else:
                r = r -1

if __name__ == '__main__':
    obj = Solution()
    numbers = [0, 0, 3, 4]
    target = 0
    # [1,2]
    print(obj.twoSum(numbers, target))
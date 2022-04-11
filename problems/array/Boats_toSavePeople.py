from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo =0
        hi = len(people) -1
        boats = 0

        while lo <= hi:
            if people[lo] + people[hi] <=limit:
                lo = lo +1
                hi = hi -1
            else:
                hi = hi - 1
            boats = boats + 1
        return boats




if __name__ == '__main__':
    obj = Solution()
    people = [3, 5, 3, 4]
    limit = 5
    print(obj.numRescueBoats(people, limit))
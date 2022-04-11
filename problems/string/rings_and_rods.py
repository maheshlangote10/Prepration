import collections

class Solution:
    def countPoints(self, rings: str) -> int:
        data = collections.Counter(rings)
        # print(data)
        for i in range(0,len(rings),2):

            data[i[1]] = data[i]

        print(data)

if __name__ == '__main__':
    obj = Solution()
    rings = "B0B6G0R6R0R6G9"
    print(obj.countPoints(rings))
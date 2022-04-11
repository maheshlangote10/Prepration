from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # res = 0
        # n = len(costs)
        # mid = n//2
        # i = 0
        # print(n, mid)
        # for costA, costB in costs:
        #     if i<mid:
        #         print("costA", costA)
        #         res += costA
        #     else:
        #         print("costB ", costB)
        #         res += costB
        #     i +=1
        # return res
        sum, length = 0, len(costs)
        num3 = [[(costs[i][0] - costs[i][1]), i] for i in range(length)]
        nums3 = sorted(num3, key=lambda x: x[0])
        print("num3", num3)
        for i in range(length // 2):
            a = costs[nums3[i][1]][0]
            print("a=",a)
            b = costs[nums3[i + (length // 2)][1]][1]
            print("b=",b)
            sum += a + b
            print("sum", sum)
        return sum

if __name__ == '__main__':
    obj = Solution()
    # costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    print(obj.twoCitySchedCost(costs))

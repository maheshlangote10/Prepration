from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = prices[0]
        for i in range(len(prices)):
            min_profit = min(min_profit, prices[i])
            profit =  prices[i] - min_profit
            max_profit = max(max_profit, profit)
        return max_profit




if __name__ == '__main__':
    obj = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(obj.maxProfit(prices))
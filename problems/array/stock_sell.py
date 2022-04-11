class Solution:

    def maxProfit(self, prices):
       buy =prices[0]
       sell = 0

       for i in range(len(prices)):
           buy = min(buy, prices[i])
           profit = prices[i] - buy
           sell = max(profit, sell)
       return sell

if __name__ == '__main__':
    obj = Solution()
    arr = [5,2,6,1,4]
    print(obj.maxProfit(arr))




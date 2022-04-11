
class Solution:

    def getMaxSumSubArrayOfKSize(self, arr, k):
        maxSum = 0
        data = dict()
        for i in range(len(arr)-k):
            winSum = 0
            for j in range(i, k+i):
                winSum = winSum + arr[j]
            maxSum = max(maxSum, winSum)
            if maxSum not in data:
                data[maxSum] = arr[i:i+k]
        return (maxSum, data[maxSum])

    def getSlidWindowSolution(self, arr, k):
        winSum = sum(arr[:k])
        maxSum = 0
        for i in range(k, len(arr)):
            winSum = winSum + arr[i] - arr[i - k]
            maxSum = max(maxSum, winSum)
        return maxSum

if __name__ == '__main__':
    obj = Solution()
    arr = [1,9,-1,-2, 7, 3, -1,2]
    print(obj.getMaxSumSubArrayOfKSize(arr, 4))
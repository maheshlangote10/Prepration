
class Solution:

    def getPair(self, arr):
        l = len(arr)
        d = dict()

        for i in range(l-1):
            for j in range(i+1, l):
                sum = arr[i] + arr[j]
                if sum not in d:
                    d[sum] = (arr[i], arr[j])
                else:
                    print("d", d)
                    print(d[sum], arr[i], arr[j])
                    break



if __name__ == '__main__':
    obj = Solution()
    data = [3, 4, 7, 1, 2, 9, 8]
    print(obj.getPair(data))

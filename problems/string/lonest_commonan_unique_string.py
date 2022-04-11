
class Solution:


    def findLongestUniqueSring(self, s:str)->int:
        n = len(s)
        res = 0
        for i in range(n):
            visited = [0] * 256
            for j in range(i,n):
                if visited[ord(s[j])] == True:
                    break
                else:
                    res = max(res,j-i+1)
                    visited[ord(s[j])] = True
            print(visited)
            print(s[i])
            visited[ord(s[i])] = False
        return res



if __name__ == '__main__':
    obj = Solution()
    s = 'geeksforgeeks'
    print(obj.findLongestUniqueSring(s))
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        d = []

        for i in range(0,len(s),k):
            temp = s[i:i+k]
            if len(temp)<k:
                fill_count = k-len(temp)
                temp = temp + fill*fill_count
            d.append(temp)
        return d


if __name__ == '__main__':
    obj = Solution()
    s = "ab"
    k = 3
    fill = "x"
    print(obj.divideString(s,k,fill))
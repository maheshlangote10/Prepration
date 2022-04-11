from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat[0]), len(mat)
        target_len = r*c
        if target_len !=  m * n:
            return mat
        output = [[ 0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(m):
            for j in range(n):
                print("K =",k)
                print("k//c ",k//c)
                print("k%c",k%c)
                output[k//c][k%c] = mat[i][j]
                k = k + 1
        return output


if __name__ == "__main__":
    obj = Solution()
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(obj.matrixReshape(mat, r, c))

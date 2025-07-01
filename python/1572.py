class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        i = 0
        j = len(mat) - 1
        for k in range(len(mat)):
            if i == j:
                ans += mat[k][i]
            else:
                ans += mat[k][i] + mat[k][j]
            i += 1
            j -= 1
        return ans 
        

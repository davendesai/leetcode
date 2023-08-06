class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])

        if r * c != ROWS * COLS:
            return mat

        res = [[0 for c in range(c)] for r in range(r)]
        res_i, res_j = 0, 0

        for i in range(ROWS):
            for j in range(COLS):
                res[res_i][res_j] = mat[i][j]
                res_j += 1
                if res_j == c:
                    res_i += 1
                    res_j = 0
        return res


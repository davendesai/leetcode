class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        def maxLocal(i, j):
            res = grid[i][j]
            for dx, dy in dirs:
               res = max(res, grid[i+dx][j+dy])
            return res

        dim = len(grid) - 2
        res = [[0 for _ in range(dim)] for _ in range(dim)]

        for i in range(dim):
            for j in range(dim):
                res[i][j] = maxLocal(i+1, j+1)
        return res 


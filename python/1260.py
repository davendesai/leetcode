class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def gridToInter(i, j):
            return i * n + j

        def interToGrid(k):
            return (k // n, k % n)

        ret = [[0] * n for i in range(m)]
        for r in range(m):
            for c in range(n):
                interPos = (gridToInter(r, c) + k) % (m * n)
                newR, newC = interToGrid(interPos)
                ret[newR][newC] = grid[r][c]

        return ret





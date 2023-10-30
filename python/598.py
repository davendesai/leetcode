"""
# Naive
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        high = 0
        for op in ops:
            for i in range(op[0]):
                for j in range(op[1]):
                    grid[i][j] += 1
                    high = max(high, grid[i][j])

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == high:
                    total += 1
        return total
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
            
        min_x = min([op[0] for op in ops])
        min_y = min([op[1] for op in ops])
        return min_x * min_y

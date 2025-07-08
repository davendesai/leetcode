"""
    b1  b2  b3  b4  b5
a1                       -inf
a2
a3
a4
     0
"""
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        @cache
        def dp(i, j):
            if i == 4:
                return 0
            if j == len(b):
                return float('-inf')
            
            take = a[i] * b[j] + dp(i+1, j+1)
            skip = dp(i, j+1)

            return max(take, skip)

        return dp(0, 0)

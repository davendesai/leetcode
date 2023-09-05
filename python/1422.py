class Solution:
    def maxScore(self, s: str) -> int:
        pivot = 1
        maxS = -1
        while pivot < len(s):
            left, right = s[:pivot], s[pivot:]
            scoreL = sum(1 for c in left if c == '0')
            scoreR = sum(1 for c in right if c == '1')
            maxS = max(maxS, scoreL + scoreR)
            pivot += 1
        return maxS


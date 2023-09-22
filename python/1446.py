class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j
        return ans


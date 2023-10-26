class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        cnt, i = 0, 0
        while i + 3 <= len(s):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                cnt += 1
            i += 1
        return cnt



class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val, cnt = 0, 0
        for idx, c in enumerate(s[::-1]):
            if c == '0':
                cnt += 1
            else:
                if val + (1 << cnt) <= k:
                    val += (1 << cnt)
                    cnt += 1
        return cnt

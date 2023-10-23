class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1: return
        n = len(s) // 2
        i, j = 0, len(s) - 1
        while n > 0:
            s[i], s[j] = s[j], s[i]
            n -= 1
            i += 1
            j -= 1


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i, j = 0, len(s) - 1
        res = list(s)

        while i < j:
            if ord(res[i]) < ord(res[j]):
                res[j] = res[i]
            elif ord(res[i]) > ord(res[j]):
                res[i] = res[j]
            i += 1
            j -= 1
        return "".join(res)


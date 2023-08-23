class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ret = -1
        idxs = {}

        for i, c in enumerate(s):
            if c in idxs:
                ret = max(ret, i - idxs[c] - 1)
            else:
                idxs[c] = i

        return ret


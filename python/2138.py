class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        i = 0

        while i + k < len(s):
            group = s[i:i+k]
            res.append(group)
            i += k

        last = s[i:]
        last += fill * (k - len(last))
        res.append(last)

        return res



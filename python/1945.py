class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ""
        for c in s:
            convert += str(ord(c) - ord('a') + 1)
        convert = int(convert)

        def transform(n):
            res = 0
            for c in str(n):
                res += int(c)
            return res

        for i in range(k):
            convert = transform(convert)
        return convert

        


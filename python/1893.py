class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for x in range(left, right + 1):
            s.add(x)

        for i, j in ranges:
            for y in range(i, j + 1):
                if y in s:
                    s.remove(y)

        return len(s) == 0

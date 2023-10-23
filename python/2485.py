class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n * (n + 1)) // 2
        x = total ** 0.5
        return int(x) if int(x) == x else -1


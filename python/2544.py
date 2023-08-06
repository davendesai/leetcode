class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0

        for idx, c in enumerate(str(n)):
            if idx % 2 == 0:
                sum += int(c)
            else:
                sum -= int(c)

        return sum


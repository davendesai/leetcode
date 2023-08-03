class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = -1
        for i in range(len(num) - 1, -1, -1):
            if not int(num[i]) % 2 == 0:
                odd = i
                break

        if odd == -1:
            return ""
        return num[:odd + 1]


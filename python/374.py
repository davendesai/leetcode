# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            m = low + (high - low) // 2
            res = guess(m)

            if res == 0:
                return m

            if res == -1:
                high = m - 1
            else:
                low = m + 1


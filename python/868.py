class Solution:
    def binaryGap(self, n: int) -> int:
        binStr = ""
        while n > 0:
            binStr += str(n & 1)
            n >>= 1
        binStr = binStr[::-1]

        looking = False
        last, dist = -1, 0
        for i in range(len(binStr)):
            if binStr[i] == '1':
                if looking:
                    dist = max(dist, i - last)
                else:
                    looking = True
                last = i

        return dist


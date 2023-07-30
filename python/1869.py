class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeroes, ones = 0, 0
        maxZ, maxO = 0, 0

        for c in s:
            if c == '0':
                ones = 0
                zeroes += 1
                maxZ = max(maxZ, zeroes)
            else:
                zeroes = 0
                ones += 1
                maxO = max(maxO, ones)

        return maxO > maxZ


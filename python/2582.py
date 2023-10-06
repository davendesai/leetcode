class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        i = time % (n - 1)

        if rounds % 2 == 0:
            return i + 1
        return n - i


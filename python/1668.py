class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        lW, lS = len(word), len(sequence)

        if lW == lS and word == sequence: return 1
        elif lW > lS: return 0

        for i in range(lS // lW, -1, -1):
            if sequence.find(word * i) != -1: return i

        return 0


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        occurences = set()

        for c in s:
            if c in occurences:
                return c
            occurences.add(c)


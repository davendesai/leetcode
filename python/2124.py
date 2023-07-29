class Solution:
    def checkString(self, s: str) -> bool:
        foundA = False
        for c in reversed(s):
            if c == 'a':
                foundA = True

            if foundA and c == 'b':
                return False
        return True


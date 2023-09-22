class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1: return "a"
        if n == 2: return "ab"
        if n % 2 == 0:
            return "a"*(n-1) + "b"

        return "c" + self.generateTheString(n-1)
        

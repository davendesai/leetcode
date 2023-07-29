class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        return n - 1
        
# n 
# n-1 factors(n-1)
# n-2 factors(n-2)
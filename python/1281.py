class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        for c in str(n):
            product *= int(c)
            sum += int(c)
        return product - sum
        

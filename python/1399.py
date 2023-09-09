class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digitSum(n):
            total = 0
            for c in str(n):
                total += int(c)
            return total

        sums = {}
        for i in range(n):
            sumD = digitSum(i + 1)
            currT = sums.get(sumD, 0)
            sums[sumD] = currT + 1
        
        maxS = max(sums.values())
        return sum(1 for i in sums.values() if i == maxS)


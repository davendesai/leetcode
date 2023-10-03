class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt, total = 0, 0
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                cnt += 1
                total += n
        if cnt == 0: return 0
        return total // cnt
        


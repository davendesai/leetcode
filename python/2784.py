class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = max(nums)
        count = 0

        n = len(nums) - 1
        total = (n * (n + 1)) // 2

        for num in nums:
            if num == base:
                count += 1
            total -= num

        return total == -1 * n and count == 2


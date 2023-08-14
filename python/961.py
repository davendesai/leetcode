class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        counts = {}

        for num in nums:
            curr = counts.get(num, 0)
            curr += 1
            if curr == n:
                return num
            counts[num] = curr
            


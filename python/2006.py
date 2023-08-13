class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                diff = nums[i] - nums[j]
                if abs(diff) == k:
                    pairs += 1
        return pairs


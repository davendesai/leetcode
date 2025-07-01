class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        @cache
        def calc(idx, sum):
            if idx == len(nums):
                return False

            if sum > total // 2:
                return False
            elif sum == total // 2:
                return True

            return calc(idx+1, sum+nums[idx]) or calc(idx+1, sum)

        return calc(0, 0)
    

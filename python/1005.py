class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = abs(nums[i])
                k -= 1
            else:
                break

        if k % 2 == 0:
            return sum(nums)

        return sum(nums) - 2 * min(nums)


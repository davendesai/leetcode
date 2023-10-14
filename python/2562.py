class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val = 0
        while len(nums) > 1:
            concat = str(nums[0]) + str(nums[-1])
            val += int(concat)
            nums = nums[1:-1]
        if nums:
            val += nums[0]
        return val


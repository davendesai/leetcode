class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        i, j = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                if j < i: j = i
                while j < len(nums) and nums[j] == 0:
                    j += 1
                    if j == len(nums): return
                nums[i], nums[j] = nums[j], nums[i]
            i += 1


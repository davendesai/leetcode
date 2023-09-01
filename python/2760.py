class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        length = 0

        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                curr = 1
                for j in range(i, len(nums) - 1):
                    if nums[j] % 2 != nums[j+1] % 2 and nums[j+1] <= threshold:
                        curr += 1
                    else:
                        i = j
                        break
                length = max(length, curr)
            i += 1

        return length          

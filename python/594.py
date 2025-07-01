class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # we dont care about the particular order only absolute values
        # i.e. subseq can discard values
        nums.sort()
        print(nums)
        ans = 0

        i = 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > 1:
                i += 1
            if nums[j] - nums[i] == 1:
                ans = max(ans, j - i + 1)

        return ans

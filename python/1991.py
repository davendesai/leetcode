class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            print(i)
            if i > 0:
                prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(len(nums), -1, -1):
            if i < len(nums) - 1:
                suffix[i] = suffix[i+1] + nums[i+1]

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1


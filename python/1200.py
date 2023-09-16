class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        diff = float('inf')

        for i in range(len(nums)-1):
            diff = min(diff, abs(nums[i] - nums[i+1]))

        ret = []
        for j in range(len(nums)-1):
            if nums[j] + diff == nums[j+1]:
                ret.append([nums[j], nums[j+1]])
        return ret


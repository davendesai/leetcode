class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = nums[i] + nums[j] + nums[k]
                    for x in range(k + 1, len(nums)):
                        if nums[x] == val:
                            cnt += 1
        return cnt


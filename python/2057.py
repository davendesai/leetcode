class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        res = -1
        for idx, n in enumerate(nums):
            if idx % 10 == n:
                if res == -1:
                    res = idx
                else:
                    res = min(res, idx)
        return res


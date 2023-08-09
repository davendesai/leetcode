class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minH = []
        for idx, n in enumerate(nums):
            heapq.heappush(minH, (n, idx))

        while len(minH) > k:
            heapq.heappop(minH)

        minH.sort(key=lambda t: t[1])
        return [nums[x[1]] for x in minH]


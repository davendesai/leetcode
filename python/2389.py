"""
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []

        for max_sum in queries:
            subseq_len = 0
            subseq_total = 0
            for n in nums:
                if n + subseq_total <= max_sum:
                    subseq_total += n
                    subseq_len += 1
            res.append(subseq_len)

        return res
"""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        # calculate prefix sums
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        res = []
        for max_sum in queries:
            i = 0
            while i < len(prefix) and prefix[i] <= max_sum:
                i += 1
            res.append(i)

        return res


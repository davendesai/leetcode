class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start, running = 0, 0

        for n in nums:
            diff = running + n

            if diff < 1:
                start += abs(diff) + 1
                running = 1
            else:
                running = diff

        if start == 0: start = 1
        return start


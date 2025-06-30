class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        sum = k * (k + 1) // 2
        nums.sort()
        duplicates = set()
        for n in nums:
            if n <= k and n not in duplicates:
                k += 1
                sum += k - n
                duplicates.add(n)

        return sum

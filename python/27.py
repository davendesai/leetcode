class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, insertIdx = 0, 0

        for n in nums:
            if n == val:
                k += 1
                continue
            nums[insertIdx] = n
            insertIdx += 1

        return len(nums) - k

        


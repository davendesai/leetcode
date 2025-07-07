class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def isZeroArray(k: int) -> bool:
            diff = [0 for _ in range(len(nums))]

            for i in range(k):
                li, ri, val = queries[i]

                diff[li] += val

                if ri < len(nums)-1:
                    diff[ri+1] -= val

            curr = 0
            for j in range(len(nums)):
                curr += diff[j]
                if curr < nums[j]:
                    return False

            return True
                
        if not isZeroArray(len(queries)):
            return -1

        l, r = 0, len(queries)

        while l < r:
            mid = l + (r-l)//2

            if isZeroArray(mid):
                r = mid
            else:
                l = mid +1

        return l            

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for n in nums1:
            if n not in res and n in nums2:
                res.append(n)

        return res

        


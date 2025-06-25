from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def numProductsLE(m: int) -> int:
            cnt = 0
            for n1 in nums1:
                if n1 > 0:
                    # n2 <= m / n1
                    cnt += bisect_right(nums2, m / n1)
                elif n1 < 0:
                    # nums2[0] > 0 then always neg
                    # nums2[0] < 0 then pos -> neg
                    idx = bisect_left(nums2, m / n1)
                    cnt += len(nums2) - idx
                else:
                    # 0 * n2 <= m when m >= 0
                    if m >= 0:
                        cnt += len(nums2)
            return cnt

        # vals are +/- 10**5
        low, high = -10**10, 10**10

        while low < high:
            pivot = (low + high) // 2
            cnt = numProductsLE(pivot)

            if cnt < k:
                low = pivot + 1
            else:
                high = pivot

        return low

"""
   2  5
3  6  15
4  8  20

   -4  -2   0  3
2  -8  -4   0  6
4  -16 -8   0  12

    -2  -1  0   1  2
-3   6   3  0  -3 -6
-1   2   1  0  -1 -2
 2  -4  -2  0   2  4
 4  -8  -4  0   4  8
 5  -10 -5  0   5  10

    -4  -3 -1
-3  12   9  3
-1   4   3  1
"""
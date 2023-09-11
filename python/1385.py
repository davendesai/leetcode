class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        def search(val):
            l, r = 0, len(arr2)-1
            while l <= r:
                m = l + ((r - l) // 2)
                diff = val - arr2[m]

                if abs(diff) <= d:
                    return 0

                if diff > 0:
                    l = m + 1
                else:
                    r = m - 1
            return 1

        arr2.sort()
        return sum([search(v) for v in arr1])


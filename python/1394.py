from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqs = Counter(arr)

        ans = -1
        for n in freqs:
            if n == freqs[n]:
                ans = max(ans, n)
        return ans
        

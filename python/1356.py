class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def ones(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        q = []
        for n in arr:
            heapq.heappush(q, (ones(n), n))

        res = []
        while len(q) > 0:
            res.append(heapq.heappop(q)[1])
        return res


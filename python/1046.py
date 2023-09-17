class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            h.append(-stone)
        heapq.heapify(h)

        while len(h) > 1:
            x, y = heapq.heappop(h), heapq.heappop(h)
            diff = abs(x) - abs(y)
            if diff != 0:
                heapq.heappush(h, -diff)

        if not h:
            return 0
        return -h[0]


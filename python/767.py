
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s

        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1

        heap = [(-f, c) for c, f in freqs.items()]
        heapq.heapify(heap)

        ans = ""
        while len(heap) >= 2:
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)

            ans += c1 + c2
            if f1 + 1 < 0:
                heapq.heappush(heap, (f1 + 1, c1))
            if f2 + 1 < 0:
                heapq.heappush(heap, (f2 + 1, c2))

        if heap:
            f, c = heapq.heappop(heap)
            if f <= -2:
                return ""
            ans += c

        return ans

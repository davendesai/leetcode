class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxheap = []
        for n in nums:
            heapq.heappush(maxheap, -1 * n)
        
        m1, m2 = heapq.heappop(maxheap), heapq.heappop(maxheap)
        return (m1+1) * (m2+1)


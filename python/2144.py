class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        l = sorted(cost)

        while len(l) > 2:
            total += l[-1] + l[-2]
            l = l[:-3]

        for c in l:
            total += c
        return total


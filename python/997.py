class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        rels = [[0,0] for x in range(n)]
        for t in trust:
            p1, p2 = t[0], t[1]
            rels[p1-1][0] += 1
            rels[p2-1][1] += 1

        for idx in range(len(rels)):
            r = rels[idx]
            if r[0] == 0 and r[1] == n-1:
                return idx+1
        return -1

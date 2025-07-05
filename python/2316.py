from collections import Counter

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def uf_find(id: int) -> int:
            if parent[id] != id:
                parent[id] = uf_find(parent[id])
            return parent[id]

        def uf_union(id1: int, id2: int):
            r1, r2 = uf_find(id1), uf_find(id2)
            if r1 == r2: return

            if rank[r1] < rank[r2]:
                parent[r1] = r2
                rank[r2] += 1
            else:
                parent[r2] = r1
                rank[r1] += 1
                
        for v1, v2 in edges:
            uf_union(v1, v2)
        root = [uf_find(i) for i in range(n)]
        print(root)
        
        islands = Counter(root)
        print(islands)

        if len(islands) == 1:
            return 0

        unreachable = 0
        for root_node in islands:
            n -= islands[root_node]
            unreachable += islands[root_node] * n

        return unreachable

"""
n = 4
conns = [[0,1],[1,2],[2,0],[1,3]]

0: 1 2
1: 0 2 3
2: 0 1
3: 1
"""

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(set)
        for n1, n2 in connections:
            adj[n1].add(n2)
            adj[n2].add(n1)

        clk = 0
        ident = [-1 for _ in range(n)]
        low = [-1 for _ in range(n)]
        bridges: List[List[int]] = []

        def dfs(node, par):
            nonlocal clk
            ident[node] = clk
            low[node] = clk
            clk += 1

            for neigh in adj[node]:
                # don't go back up dfs tree
                if neigh == par: continue

                # not visited
                if ident[neigh] == -1:
                    dfs(neigh, node)

                    # update fastest conn to me
                    low[node] = min(low[node], low[neigh])

                    # means back-edge cant get to node faster than thru me
                    # i.e. this conn necessary
                    if low[neigh] > ident[node]:
                        bridges.append([node, neigh])
                else:
                    # check if back-edge faster
                    low[node] = min(low[node], ident[neigh])

        dfs(0, -1)
        print(ident, low)
        return bridges
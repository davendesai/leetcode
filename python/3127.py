class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        tl = grid[0][0] + grid[0][1] + grid[1][0] + grid[1][1]
        tr = grid[0][1] + grid[0][2] + grid[1][1] + grid[1][2]
        bl = grid[1][0] + grid[1][1] + grid[2][0] + grid[2][1]
        br = grid[1][1] + grid[1][2] + grid[2][1] + grid[2][2]
        return \
            tl.count("W") >= 3 or tl.count("B") >= 3 or \
            tr.count("W") >= 3 or tr.count("B") >= 3 or \
            bl.count("W") >= 3 or bl.count("B") >= 3 or \
            br.count("W") >= 3 or br.count("B") >= 3

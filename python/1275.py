class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['.' for _ in range(3)] for _ in range(3)]

        def mark(player, row, col):
            grid[row][col] = player
            print(grid)

            if grid[0][0] == grid[1][1] == grid[2][2] == player:
                return True

            if grid[0][2] == grid[1][1] == grid[2][0] == player:
                return True
            
            if grid[0][col] == grid[1][col] == grid[2][col]:
                return True

            if grid[row][0] == grid[row][1] == grid[row][2]:
                return True

            return False
        
        for i in range(len(moves)):
            r, c = moves[i]
            if i % 2 == 0:
                if mark('X', r, c): return 'A'
            else:
                if mark('O', r, c): return 'B'

        if len(moves) == 9:
            return "Draw"

        return "Pending"


class Solution(object):
    def numMagicSquaresInside(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def isMagic(r, c):
            # 1. Check uniqueness and range 1-9
            vals = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    vals.append(grid[i][j])
            
            if sorted(vals) != list(range(1, 10)):
                return False
            
            # 2. Check Rows
            for i in range(r, r + 3):
                if sum(grid[i][c:c+3]) != 15:
                    return False
            
            # 3. Check Columns
            for j in range(c, c + 3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15:
                    return False
            
            # 4. Check Diagonals
            diag1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            diag2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
            
            return diag1 == 15 and diag2 == 15

        # Iterate through every possible top-left corner of a 3x3
        for r in range(rows - 2):
            for c in range(cols - 2):
                # Optimization: Center must be 5
                if grid[r+1][c+1] == 5:
                    if isMagic(r, c):
                        count += 1
                        
        return count

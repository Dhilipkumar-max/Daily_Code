class Solution(object):
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        # Keep track of 'X' and 'Y' counts for each column as we move down the rows
        col_counts_x = [0] * cols
        col_counts_y = [0] * cols
        
        ans = 0
        
        for r in range(rows):
            curr_x = 0
            curr_y = 0
            
            for c in range(cols):
                # Update the column totals for the current row
                if grid[r][c] == 'X':
                    col_counts_x[c] += 1
                elif grid[r][c] == 'Y':
                    col_counts_y[c] += 1
                    
                # Accumulate the column totals to get the submatrix totals up to (r, c)
                curr_x += col_counts_x[c]
                curr_y += col_counts_y[c]
                
                # Check if the submatrix from (0,0) to (r,c) is valid
                if curr_x == curr_y and curr_x > 0:
                    ans += 1
                    
        return ans

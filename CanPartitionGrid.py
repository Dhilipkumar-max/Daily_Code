class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Arrays to store the sum of each row and each column
        row_sums = [0] * m
        col_sums = [0] * n
        
        # Calculate row sums and col sums in a single pass over the grid
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                row_sums[i] += val
                col_sums[j] += val
                
        total_sum = sum(row_sums) # Could also be sum(col_sums)
        
        # If the total sum is odd, it's impossible to split it into equal halves
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # Check for a valid horizontal cut
        current_sum = 0
        # We stop at m - 1 because the bottom section must be non-empty
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True
                
        # Check for a valid vertical cut
        current_sum = 0
        # We stop at n - 1 because the right section must be non-empty
        for j in range(n - 1):
            current_sum += col_sums[j]
            if current_sum == target:
                return True
                
        # If no cuts matched the target sum, it's impossible
        return False

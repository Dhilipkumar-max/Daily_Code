class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        # Start from the bottom-left corner
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # If grid[row][col] is negative, the whole rest 
                # of the row to the right is also negative.
                count += (n - col)
                # Move up to the next row
                row -= 1
            else:
                # If positive, move right to find a negative number
                col += 1
                
        return count

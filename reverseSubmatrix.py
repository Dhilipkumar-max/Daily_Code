class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Iterate through the top half of the submatrix rows
        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i
            
            # Swap elements column by column within the submatrix width
            for j in range(k):
                col = y + j
                # Swap the top element with the bottom element
                grid[top_row][col], grid[bottom_row][col] = grid[bottom_row][col], grid[top_row][col]
                
        return grid

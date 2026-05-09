class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        num_layers = min(m, n) // 2
        
        for c in range(num_layers):
            # 1. Extract the elements of the current layer in clockwise order
            layer = []
            
            # Top row
            for j in range(c, n - c):
                layer.append(grid[c][j])
            # Right column
            for i in range(c + 1, m - c):
                layer.append(grid[i][n - 1 - c])
            # Bottom row
            for j in range(n - 2 - c, c - 1, -1):
                layer.append(grid[m - 1 - c][j])
            # Left column
            for i in range(m - 2 - c, c, -1):
                layer.append(grid[i][c])
                
            # 2. Calculate effective rotations to avoid redundant looping
            l_len = len(layer)
            rot = k % l_len
            
            # Rotate layer counter-clockwise
            layer = layer[rot:] + layer[:rot]
            
            # 3. Put the rotated elements back into the grid
            idx = 0
            
            # Top row
            for j in range(c, n - c):
                grid[c][j] = layer[idx]
                idx += 1
            # Right column
            for i in range(c + 1, m - c):
                grid[i][n - 1 - c] = layer[idx]
                idx += 1
            # Bottom row
            for j in range(n - 2 - c, c - 1, -1):
                grid[m - 1 - c][j] = layer[idx]
                idx += 1
            # Left column
            for i in range(m - 2 - c, c, -1):
                grid[i][c] = layer[idx]
                idx += 1
                
        return grid

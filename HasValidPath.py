import collections

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        if not grid or not grid[0]:
            return False
            
        m, n = len(grid), len(grid[0])
        
        # Define directional vectors: (row_change, col_change)
        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)
        
        # Map each street type to the directions we can exit towards
        exits = {
            1: [LEFT, RIGHT],
            2: [UP, DOWN],
            3: [LEFT, DOWN],
            4: [RIGHT, DOWN],
            5: [LEFT, UP],
            6: [RIGHT, UP]
        }
        
        # Map the direction we are traveling to the valid street types that can accept us
        # e.g., if we travel UP, the cell above us must accept a DOWN connection.
        valid_entries = {
            UP: {2, 3, 4},
            DOWN: {2, 5, 6},
            LEFT: {1, 4, 6},
            RIGHT: {1, 3, 5}
        }
        
        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            r, c = queue.popleft()
            
            # If we've reached the bottom-right corner, we found a valid path
            if r == m - 1 and c == n - 1:
                return True
            
            current_street = grid[r][c]
            
            # Explore all possible exits from the current street tile
            for dr, dc in exits[current_street]:
                nr, nc = r + dr, c + dc
                
                # Check if the next cell is within bounds and hasn't been visited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    neighbor_street = grid[nr][nc]
                    
                    # Verify the neighbor cell connects back to our current direction
                    if neighbor_street in valid_entries[(dr, dc)]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False

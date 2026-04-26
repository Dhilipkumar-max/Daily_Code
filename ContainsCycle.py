from collections import deque

class Solution(object):
    def containsCycle(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        # 2D array to keep track of visited cells
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    # Start BFS from this unvisited cell
                    # Queue stores: (current_row, current_col, parent_row, parent_col)
                    queue = deque([(r, c, -1, -1)])
                    visited[r][c] = True
                    
                    while queue:
                        curr_r, curr_c, parent_r, parent_c = queue.popleft()
                        
                        # Explore all 4 adjacent directions
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # Ensure the next cell is within bounds and has the same character
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[curr_r][curr_c]:
                                if not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    queue.append((nr, nc, curr_r, curr_c))
                                elif nr != parent_r or nc != parent_c:
                                    # If the adjacent cell is already visited and is NOT the parent, a cycle exists
                                    return True
        
        # If all components are explored without finding a cycle
        return False

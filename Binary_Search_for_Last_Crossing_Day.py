from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        def canCross(day):
            # Create a grid for the current day
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            queue = deque()
            visited = set()
            
            # Start BFS from all land cells in the first row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))
            
            while queue:
                r, c = queue.popleft()
                
                # If we reached the last row, a path exists
                if r == row - 1:
                    return True
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and \
                       grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return False

        # Binary search for the last possible day
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if canCross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

class Solution(object):
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        top_sums = []

        def add_sum(val):
            # Only add distinct values
            if val not in top_sums:
                top_sums.append(val)
                # Sort descending and keep only top 3
                top_sums.sort(reverse=True)
                if len(top_sums) > 3:
                    top_sums.pop()

        # Iterate through every cell acting as the TOP corner of a rhombus
        for r in range(m):
            for c in range(n):
                # Case 1: Rhombus of area 0 (just the single cell)
                add_sum(grid[r][c])

                # Case 2: Rhombus of area > 0
                L = 1
                # Ensure the bottom, left, and right corners fit within the grid
                while r + 2 * L < m and c - L >= 0 and c + L < n:
                    curr_sum = 0
                    x, y = r, c
                    
                    # 1. Traverse Top to Right edge
                    for _ in range(L):
                        curr_sum += grid[x][y]
                        x += 1
                        y += 1
                    
                    # 2. Traverse Right to Bottom edge
                    for _ in range(L):
                        curr_sum += grid[x][y]
                        x += 1
                        y -= 1
                        
                    # 3. Traverse Bottom to Left edge
                    for _ in range(L):
                        curr_sum += grid[x][y]
                        x -= 1
                        y -= 1
                        
                    # 4. Traverse Left to Top edge
                    for _ in range(L):
                        curr_sum += grid[x][y]
                        x -= 1
                        y += 1

                    add_sum(curr_sum)
                    L += 1 # Expand the rhombus size

        return top_sums

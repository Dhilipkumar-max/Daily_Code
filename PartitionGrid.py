from collections import Counter

class Solution(object):
    def canPartitionGrid(self, grid):
        M, N = len(grid), len(grid)
        total_sum = sum(sum(row) for row in grid)
        
        # Global frequency map to check existence in Section B
        total_freq = Counter()
        for r in range(M):
            for val in grid[r]:
                total_freq[val] += 1
                
        def is_removable(target, r1, c1, r2, c2, section_freq):
            """
            Checks if 'target' exists in the rectangle (r1,c1) to (r2,c2)
            such that its removal maintains connectivity.
            """
            h = r2 - r1 + 1
            w = c2 - c1 + 1
            
            # Case 1: 2D block (all cells are removable)
            if h > 1 and w > 1:
                return section_freq[target] > 0
            # Case 2: Horizontal strip (only ends are removable)
            if h == 1 and w > 1:
                return target == grid[r1][c1] or target == grid[r1][c2]
            # Case 3: Vertical strip (only ends are removable)
            if h > 1 and w == 1:
                return target == grid[r1][c1] or target == grid[r2][c1]
            # Case 4: Single cell
            return target == grid[r1][c1]

        # --- Horizontal Cuts ---
        curr_top_sum = 0
        curr_top_freq = Counter()
        for i in range(M - 1):
            for val in grid[i]:
                curr_top_freq[val] += 1
            curr_top_sum += sum(grid[i])
            
            sA, sB = curr_top_sum, total_sum - curr_top_sum
            diff = sA - sB
            
            if diff == 0: return True
            if diff > 0: # Try removing from A
                if is_removable(diff, 0, 0, i, N-1, curr_top_freq): return True
            else: # Try removing from B (diff is negative)
                target = abs(diff)
                # B freq = total - A
                b_freq_val = total_freq[target] - curr_top_freq[target]
                if is_removable(target, i+1, 0, M-1, N-1, {target: b_freq_val}): return True

        # --- Vertical Cuts ---
        curr_left_sum = 0
        curr_left_freq = Counter()
        for j in range(N - 1):
            for r in range(M):
                val = grid[r][j]
                curr_left_freq[val] += 1
                curr_left_sum += val
            
            sA, sB = curr_left_sum, total_sum - curr_left_sum
            diff = sA - sB
            
            if diff == 0: return True
            if diff > 0:
                if is_removable(diff, 0, 0, M-1, j, curr_left_freq): return True
            else:
                target = abs(diff)
                b_freq_val = total_freq[target] - curr_left_freq[target]
                if is_removable(target, 0, j+1, M-1, N-1, {target: b_freq_val}): return True

        return False

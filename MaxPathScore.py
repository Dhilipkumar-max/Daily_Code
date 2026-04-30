class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # The maximum cost we can ever encounter is bounded by the path length.
        # Max path length is m + n - 1. Since grid[0][0] == 0, max cost is m + n - 2.
        # We cap K to avoid allocating and computing unnecessary states.
        K = min(k, m + n - 2)
        
        # dp[c][cost] stores the maximum score to reach column `c` with exact `cost`
        # We only need 1D arrays to represent the previous row to save memory.
        dp = [[-1] * (K + 1) for _ in range(n)]
        
        for r in range(m):
            # new_dp represents the current row we are computing
            new_dp = [[-1] * (K + 1) for _ in range(n)]
            
            for c in range(n):
                # Base Case: Top-Left cell
                if r == 0 and c == 0:
                    new_dp[c][0] = 0
                    continue
                    
                cell_val = grid[r][c]
                cell_score = cell_val
                cell_cost = 1 if cell_val > 0 else 0
                
                # Check valid transitions based on cost limits
                for cost in range(cell_cost, K + 1):
                    prev_cost = cost - cell_cost
                    
                    # Fetch max score from the cell to the Left
                    val_left = new_dp[c-1][prev_cost] if c > 0 else -1
                    
                    # Fetch max score from the cell Above
                    val_up = dp[c][prev_cost] if r > 0 else -1
                    
                    # Determine the best incoming path
                    best_prev = val_left if val_left > val_up else val_up
                    
                    if best_prev != -1:
                        new_dp[c][cost] = best_prev + cell_score
                        
            # Move down to the next row
            dp = new_dp
            
        # The answer is the highest score found at the bottom-right cell (dp[n-1]) across any valid cost.
        ans = max(dp[n-1])
        
        return ans if ans != -1 else -1


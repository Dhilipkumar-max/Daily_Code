class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid)
        MOD = 10**9 + 7
        
        # We need two tables: one for the highest possible product (max)
        # and one for the lowest (min), because a low negative * a negative cell = a high positive.
        max_dp = [ * n for _ in range(m)]
        min_dp = [ * n for _ in range(m)]
        
        # Starting point
        max_dp = min_dp = grid
        
        # Initialize first column (can only come from above)
        for i in range(1, m):
            max_dp[i] = min_dp[i] = max_dp[i-1] * grid[i]
            
        # Initialize first row (can only come from left)
        for j in range(1, n):
            max_dp[j] = min_dp[j] = max_dp[j-1] * grid[j]
            
        # Fill the grid
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                # Possible products at this cell:
                # 1. Previous Max from above * current
                # 2. Previous Min from above * current
                # 3. Previous Max from left * current
                # 4. Previous Min from left * current
                options = [
                    max_dp[i-1][j] * val,
                    min_dp[i-1][j] * val,
                    max_dp[i][j-1] * val,
                    min_dp[i][j-1] * val
                ]
                max_dp[i][j] = max(options)
                min_dp[i][j] = min(options)
        
        res = max_dp[m-1][n-1]
        
        # Return -1 if the best we can do is negative, otherwise apply the modulo
        return res % MOD if res >= 0 else -1

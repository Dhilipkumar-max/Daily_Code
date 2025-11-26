class Solution(object):
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[j][r] = number of ways to reach this row at column j with sum % k == r
        dp = [[0] * k for _ in range(n)]
        
        dp[0][grid[0][0] % k] = 1
        
        # Fill first row
        for j in range(1, n):
            val = grid[0][j]
            for r in range(k):
                if dp[j - 1][r]:
                    dp[j][(r + val) % k] = (dp[j][(r + val) % k] + dp[j - 1][r]) % MOD
        
        # Process remaining rows
        for i in range(1, m):
            new_dp = [[0] * k for _ in range(n)]
            
            # First column of each row
            val = grid[i][0]
            for r in range(k):
                if dp[0][r]:
                    new_dp[0][(r + val) % k] = (new_dp[0][(r + val) % k] + dp[0][r]) % MOD
            
            # Rest of the row
            for j in range(1, n):
                val = grid[i][j]
                for r in range(k):
                    if new_dp[j - 1][r]:     # from left
                        new_dp[j][(r + val) % k] = (new_dp[j][(r + val) % k] + new_dp[j - 1][r]) % MOD
                    if dp[j][r]:             # from top
                        new_dp[j][(r + val) % k] = (new_dp[j][(r + val) % k] + dp[j][r]) % MOD
            
            dp = new_dp
        
        return dp[n - 1][0] % MOD

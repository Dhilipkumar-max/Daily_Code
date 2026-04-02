class Solution(object):
    def maximumAmount(self, coins):
        m = len(coins)
        n = len(coins[0])
        
        # Initialize 3D DP table with negative infinity
        # dp[i][j][k] -> max coins at (i, j) with k neutralizations remaining
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base Case: Starting cell (0, 0)
        # 0 uses left
        dp[0][0][0] = coins[0][0]
        # 1 use left (if negative, we can neutralize it)
        dp[0][0][1] = max(coins[0][0], 0)
        # 2 uses left (can't use 2 on one cell, but we carry the option)
        dp[0][0][2] = max(coins[0][0], 0)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    res = -float('inf')
                    
                    # Option 1: Coming from Top
                    if i > 0:
                        # Case A: Don't use a neutralization at current cell
                        res = max(res, dp[i-1][j][k] + coins[i][j])
                        # Case B: Use a neutralization at current cell (if negative and k > 0)
                        if k > 0 and coins[i][j] < 0:
                            res = max(res, dp[i-1][j][k-1])
                            
                    # Option 2: Coming from Left
                    if j > 0:
                        # Case A: Don't use a neutralization
                        res = max(res, dp[i][j-1][k] + coins[i][j])
                        # Case B: Use a neutralization
                        if k > 0 and coins[i][j] < 0:
                            res = max(res, dp[i][j-1][k-1])
                    
                    dp[i][j][k] = res
                    
        # The answer is the max profit at the bottom-right corner with any number of uses
        return max(dp[m-1][n-1])


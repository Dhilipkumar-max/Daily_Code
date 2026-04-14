class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # Sort robots and factories by position (crucial for optimal assignment)
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        # dp[i][j] = minimum cost to repair first i robots using first j factories
        # We use a 2D list with large value as infinity
        INF = 10**18
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots require 0 distance
        for j in range(m + 1):
            dp[0][j] = 0
        
        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Option 1: Skip this factory (use previous factories only)
                dp[i][j] = dp[i][j - 1]
                
                # Option 2: Use current factory (factory[j-1]) to repair some robots
                # We try assigning 1 to limit robots from the end of current prefix
                pos = factory[j - 1][0]
                limit = factory[j - 1][1]
                
                cost = 0
                for k in range(1, min(limit, i) + 1):
                    # Assign the last k robots (i-k to i-1) to this factory
                    # Since everything is sorted, the optimal is to assign a consecutive segment
                    cost += abs(robot[i - k] - pos)
                    
                    if dp[i - k][j - 1] != INF:
                        dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cost)
        
        return dp[n][m]

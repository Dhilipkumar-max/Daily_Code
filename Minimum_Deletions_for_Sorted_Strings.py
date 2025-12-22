class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        
        # dp[j] will store the length of the longest valid subsequence 
        # of columns ending at index j.
        dp = [1] * m
        
        for j in range(1, m):
            for i in range(j):
                # Check if column j can follow column i
                # Every row must satisfy the non-decreasing condition
                if all(strs[k][i] <= strs[k][j] for k in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # Max columns kept
        max_kept = max(dp)
        
        # Minimum deletions = total columns - maximum columns we can keep
        return m - max_kept

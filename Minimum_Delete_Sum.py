class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        
        # dp[i][j] will store the maximum ASCII sum of a common subsequence 
        # using s1[0...i-1] and s2[0...j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    # If characters match, add their ASCII value to the diagonal result
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    # If they don't match, take the maximum from the top or left cell
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Calculate total ASCII sum of both strings
        total_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        
        # Result is total sum minus twice the shared common sum
        return total_sum - 2 * dp[m][n]

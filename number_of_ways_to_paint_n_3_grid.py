class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Initial states for n = 1
        aba = 6
        abc = 6
        
        for _ in range(n - 1):
            # Calculate next states based on transition rules
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD

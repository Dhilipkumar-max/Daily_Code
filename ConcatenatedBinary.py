class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        res = 0
        bit_length = 0
        
        for i in range(1, n + 1):
            # If i is a power of 2, the number of bits increases
            # (i & (i - 1)) == 0 is a quick way to check for powers of 2
            if i & (i - 1) == 0:
                bit_length += 1
            
            # Shift the result and add the current number
            res = ((res << bit_length) | i) % MOD
            
        return res

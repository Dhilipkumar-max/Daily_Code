class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        # We must iterate exactly 32 times for a 32-bit integer
        for _ in range(32):
            # Shift res left to make room, then add the LSB of n
            res = (res << 1) | (n & 1)
            # Shift n right to process the next bit
            n >>= 1
            
        return res

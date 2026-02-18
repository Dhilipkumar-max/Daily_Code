class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Right shift n by 1 and XOR with n. 
        # If n has alternating bits, x will be a sequence of all 1s.
        x = n ^ (n >> 1)
        
        # Check if x is all 1s. 
        # If x is all 1s, x + 1 will flip all those 1s to 0s and carry over a 1.
        # So, x & (x + 1) must be 0.
        return (x & (x + 1)) == 0

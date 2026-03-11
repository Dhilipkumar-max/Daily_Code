class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Edge case for 0
        if n == 0:
            return 1
            
        # Create a mask of 1s the same length as n's binary representation
        # n.bit_length() gives the number of bits required to represent n
        # (1 << length) - 1 creates a string of 1s of that exact length
        mask = (1 << n.bit_length()) - 1
        
        # XOR n with the mask to flip all bits
        return n ^ mask

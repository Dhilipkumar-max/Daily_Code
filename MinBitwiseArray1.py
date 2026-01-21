class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            if n == 2:
                # The only even prime is 2. 
                # x OR (x+1) always results in an odd number (unless x+1 is 0),
                # because (x+1) will always have the 0th bit different from x.
                ans.append(-1)
            else:
                # Find the first '0' bit from the right in n's binary form.
                # Since n is a prime > 2, it is always odd (ends in 1).
                # We are looking for the end of the trailing sequence of 1s.
                
                # Trick: (n + 1) & -(n + 1) gives the power of 2 
                # corresponding to the first zero bit in n.
                # Example: n = 11 (1011), n+1 = 12 (1100). 
                # Lowest set bit of 12 is 4 (100).
                first_zero_bit_mask = (n + 1) & -(n + 1)
                
                # We flip the bit immediately to the right of that zero.
                # n - (mask >> 1)
                ans.append(n - (first_zero_bit_mask >> 1))
        
        return ans

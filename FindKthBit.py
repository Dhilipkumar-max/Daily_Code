class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Base case: S1 is always "0"
        if n == 1:
            return "0"
        
        # Calculate the length of Sn: 2^n - 1
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            # It's in the first half, which is exactly Sn-1
            return self.findKthBit(n - 1, k)
        else:
            # It's in the second half. 
            # We find the mirrored position in the first half
            mirrored_k = length - k + 1
            res = self.findKthBit(n - 1, mirrored_k)
            # Flip the bit ("0" -> "1", "1" -> "0")
            return "1" if res == "0" else "0"

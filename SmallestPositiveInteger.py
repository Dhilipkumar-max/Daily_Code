class Solution(object):
    def smallestRepunitDivByK(self, k):
        # If k has factors 2 or 5, no repunit can divide it
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        length = 0
        
        # Maximum iterations needed is k (pigeonhole principle)
        for _ in range(k):
            remainder = (remainder * 10 + 1) % k
            length += 1
            if remainder == 0:
                return length
        
        return -1  # Should never happen for valid cases

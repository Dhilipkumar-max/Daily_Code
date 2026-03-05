class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # count1 will track mismatches for pattern "0101..."
        count1 = 0
        
        for i in range(n):
            # For pattern starting with '0': 
            # Even indices should be '0', odd indices should be '1'
            if i % 2 == 0:
                if s[i] != '0':
                    count1 += 1
            else:
                if s[i] != '1':
                    count1 += 1
        
        # The number of operations for the "1010..." pattern 
        # is simply the total length minus count1.
        return min(count1, n - count1)

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Total unique codes of length k is 2^k
        required_count = 1 << k
        seen_codes = set()
        
        # Iterate through s to find all substrings of length k
        # We stop at len(s) - k + 1 because a window of size k 
        # cannot start later than that.
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen_codes.add(substring)
            
            # Optimization: if we've found all codes, stop early
            if len(seen_codes) == required_count:
                return True
                
        return False

class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base case: if the string is empty or very short
        if not s:
            return ""
        
        count = 0
        i = 0
        res = []
        
        # Split s into its immediate special substrings
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            # When count hits 0, we've found a complete special substring
            if count == 0:
                # Recursively process the nested part: s[i+1 : j]
                # Then wrap it back in its original '1' and '0'
                inner_optimized = self.makeLargestSpecial(s[i + 1:j])
                res.append("1" + inner_optimized + "0")
                i = j + 1
        
        # Sort the special substrings descending to get the lexicographically largest result
        res.sort(reverse=True)
        
        return "".join(res)

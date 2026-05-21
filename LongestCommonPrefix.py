class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()
        for x in arr1:
            while x > 0:
                prefixes.add(x)
                x //= 10
        
        max_len = 0
        
        # Check elements in arr2 against the set of prefixes
        for y in arr2:
            length = len(str(y))
            
            # Optimization: If the current number is already shorter than or 
            # equal to our found max_len, we don't need to check it.
            if length <= max_len:
                continue
            
            while y > 0:
                # Stop checking if the remaining prefix length cannot beat max_len
                if length <= max_len:
                    break
                
                # If a match is found, record the length and move to the next number in arr2
                if y in prefixes:
                    max_len = length
                    break
                
                # Truncate the rightmost digit to check the next shorter prefix
                y //= 10
                length -= 1
                
        return max_len

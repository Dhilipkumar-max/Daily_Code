class Solution(object):
    def numberOfSubstrings(self, s):
        # Initialize the most recently seen indices for a, b, and c
        last_a = last_b = last_c = -1
        total_substrings = 0
        
        for i, char in enumerate(s):
            # Update the last seen index for the current character
            if char == 'a':
                last_a = i
            elif char == 'b':
                last_b = i
            else:
                last_c = i
            
            # Find the index of the character that was seen furthest back
            min_idx = min(last_a, last_b, last_c)
            
            # If all characters have been seen at least once
            if min_idx != -1:
                # Add the number of valid starting positions to the total
                total_substrings += min_idx + 1
                
        return total_substrings

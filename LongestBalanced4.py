class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0
        
        # Iterate through every possible starting position
        for i in range(n):
            char_counts = {}
            distinct_count = 0
            
            # Expand the substring to the right
            for j in range(i, n):
                char = s[j]
                
                # Update frequency map
                if char not in char_counts:
                    char_counts[char] = 0
                    distinct_count += 1
                char_counts[char] += 1
                
                # A substring of length L with k distinct characters 
                # is balanced if L is divisible by k and every 
                # character's count is exactly L / k.
                current_length = j - i + 1
                
                if current_length % distinct_count == 0:
                    target_freq = current_length // distinct_count
                    
                    # Check if all characters in our current map meet the target_freq
                    # Using all() is efficient here as the map size is at most 26
                    if all(count == target_freq for count in char_counts.values()):
                        max_length = max(max_length, current_length)
                        
        return max_length

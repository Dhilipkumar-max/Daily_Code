class Solution(object):
    def numberOfSpecialChars(self, word):
        # Convert the string to a set for O(1) lookups
        char_set = set(word)
        special_count = 0
        
        # Iterate through every lowercase letter in the alphabet
        for char in "abcdefghijklmnopqrstuvwxyz":
            # Check if both the lowercase and uppercase versions are in the set
            if char in char_set and char.upper() in char_set:
                special_count += 1
                
        return special_count
        

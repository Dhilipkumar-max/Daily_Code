class Solution(object):
    def numberOfSpecialChars(self, word):
        last_lower = {}
        first_upper = {}
        
        # Track the last occurrence of lowercase and first occurrence of uppercase letters
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            elif char.isupper():
                # Only record the index if we haven't seen this uppercase letter yet
                if char not in first_upper:
                    first_upper[char] = i
                    
        special_count = 0
        
        # Check all 26 lowercase English letters
        for char in "abcdefghijklmnopqrstuvwxyz":
            upper_char = char.upper()
            
            # A letter is special if both cases exist and all lowers precede the first upper
            if char in last_lower and upper_char in first_upper:
                if last_lower[char] < first_upper[upper_char]:
                    special_count += 1
                    
        return special_count

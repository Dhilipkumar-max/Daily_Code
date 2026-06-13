class Solution(object):
    def mapWordWeights(self, words, weights):
        result = []
        
        for word in words:
            # Calculate the total weight of the word
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # Take modulo 26
            mod_val = word_weight % 26
            
            # Map to reverse alphabetical order (0 -> 'z', ..., 25 -> 'a')
            # ASCII value of 'z' is 122.
            mapped_char = chr(ord('z') - mod_val)
            
            result.append(mapped_char)
            
        return "".join(result)

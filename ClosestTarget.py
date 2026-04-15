class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_dist = n  # Initialize with a value larger than any possible distance
        found = False

        for i in range(n):
            if words[i] == target:
                found = True
                # Standard absolute distance
                abs_dist = abs(i - startIndex)
                
                # Circular distance is the minimum of going left or right
                # min(direct distance, distance around the wrap-around)
                current_dist = min(abs_dist, n - abs_dist)
                
                if current_dist < min_dist:
                    min_dist = current_dist
        
        return min_dist if found else -1

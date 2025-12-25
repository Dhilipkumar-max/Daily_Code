class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        # Sort in descending order to pick the largest values first
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        # We iterate k times to pick k children
        for i in range(k):
            # The current child's happiness decreases by 'i' (the number of turns passed)
            # Use max(0, ...) to ensure happiness doesn't go below zero
            current_val = max(0, happiness[i] - i)
            
            # If the value hits 0, all subsequent children (who are less happy) 
            # will also be 0 or less, so we can stop early.
            if current_val == 0:
                break
                
            total_happiness += current_val
            
        return total_happiness

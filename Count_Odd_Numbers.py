class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # Compute base count
        count = (high - low) // 2
        
        # Add 1 if both low and high are odd
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        
        return count

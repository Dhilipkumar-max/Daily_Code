class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        negative_count = 0
        min_abs_val = float('inf')
        
        for row in matrix:
            for val in row:
                # Add the absolute value to the total sum
                abs_val = abs(val)
                total_sum += abs_val
                
                # Count negatives
                if val < 0:
                    negative_count += 1
                
                # Track the smallest absolute value
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
        
        # If there's an odd number of negatives, we must leave one value negative.
        # We choose the smallest one to minimize the loss.
        if negative_count % 2 == 1:
            return total_sum - 2 * min_abs_val
        
        return total_sum

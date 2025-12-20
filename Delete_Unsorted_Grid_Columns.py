class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # Count of columns to be deleted
        delete_count = 0
        
        # Number of rows (n) and number of columns (length of strings)
        rows = len(strs)
        cols = len(strs[0])
        
        # Iterate through each column
        for c in range(cols):
            # Check each row in the current column
            for r in range(1, rows):
                # If the character above is greater than the current character,
                # the column is not lexicographically sorted.
                if strs[r][c] < strs[r-1][c]:
                    delete_count += 1
                    # Break the inner loop to move to the next column
                    break
                    
        return delete_count

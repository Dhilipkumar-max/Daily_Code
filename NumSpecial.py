class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        
        # Step 1: Record counts of 1s in each row and column
        row_counts = [0] * m
        col_counts = [0] * n
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        # Step 2: Check each 1 to see if its row and column totals are exactly 1
        special_count = 0
        for i in range(m):
            # Optimization: If row_counts[i] isn't 1, no element in this row can be special
            if row_counts[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1:
                        if col_counts[j] == 1:
                            special_count += 1
        
        return special_count

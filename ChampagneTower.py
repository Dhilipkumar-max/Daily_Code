class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # Initialize the first row with the total amount poured
        current_row = [float(poured)]
        
        # Simulate row by row until we reach the target query_row
        for r in range(query_row):
            # The next row always has one more glass than the current row
            next_row = [0.0] * (len(current_row) + 1)
            
            # Distribute the excess from each glass in the current row
            for c in range(len(current_row)):
                # If the glass overflows, distribute the excess
                if current_row[c] > 1.0:
                    excess = (current_row[c] - 1.0) / 2.0
                    next_row[c] += excess
                    next_row[c + 1] += excess
            
            # Move down to the next row
            current_row = next_row
            
        # The glass can hold a maximum of 1.0 cup.
        # If it has more, it just means it overflowed, so we cap it at 1.0
        return min(1.0, current_row[query_glass])

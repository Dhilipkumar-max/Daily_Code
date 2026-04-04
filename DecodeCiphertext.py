class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        length = len(encodedText)
        if length == 0 or rows == 1:
            return encodedText
        
        cols = length // rows
        decoded = []
        
        # Iterate over every starting column in the first row
        for start_col in range(cols):
            # Trace the diagonal downwards: (r, start_col + r)
            for r in range(rows):
                c = start_col + r
                
                # If the column goes out of bounds, this diagonal is done
                if c >= cols:
                    break
                
                # Map 2D coordinates (r, c) to 1D index
                idx = r * cols + c
                decoded.append(encodedText[idx])
                
        # The problem states originalText has no trailing spaces
        return "".join(decoded).rstrip()

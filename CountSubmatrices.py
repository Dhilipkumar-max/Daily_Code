class Solution(object):
    def countSubmatrices(self, grid, k):
        n = len(grid[0])
        prev_row = [0] * n
        count = 0
        
        # max_c keeps track of the maximum column index we need to check.
        max_c = n 
        
        for row in grid:
            curr_row_sum = 0
            for j in range(max_c):
                # 1D prefix sum of the current row up to index j
                curr_row_sum += row[j]
                
                # Add the current row's sum to the running 2D prefix sum up to column j
                prev_row[j] += curr_row_sum
                
                if prev_row[j] <= k:
                    count += 1
                else:
                    # Since all values are >= 0, moving further right or down 
                    # will only yield sums > k. We cap the columns for future rows.
                    max_c = j
                    break
                    
        return count

class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        ans = []
        
        # Iterate over the top-left corner of every k x k submatrix
        for i in range(m - k + 1):
            row_ans = []
            for j in range(n - k + 1):
                # Use a set to capture only distinct values
                distinct_vals = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        distinct_vals.add(grid[x][y])
                
                # If there are less than 2 distinct values, the difference is 0
                if len(distinct_vals) < 2:
                    row_ans.append(0)
                else:
                    # Sort distinct values to easily find the minimum adjacent difference
                    sorted_vals = sorted(list(distinct_vals))
                    min_diff = float('inf')
                    
                    for idx in range(1, len(sorted_vals)):
                        diff = sorted_vals[idx] - sorted_vals[idx - 1]
                        if diff < min_diff:
                            min_diff = diff
                            
                    row_ans.append(min_diff)
            
            ans.append(row_ans)
            
        return ans

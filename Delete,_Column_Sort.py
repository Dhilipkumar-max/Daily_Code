class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        res = 0
        # is_sorted[i] is True if strs[i] < strs[i+1] 
        # based on columns kept so far
        is_sorted = [False] * (n - 1)
        
        for j in range(m):
            # Check if this column is "valid" to keep
            is_valid = True
            for i in range(n - 1):
                # We only care about the order if they aren't already sorted
                if not is_sorted[i] and strs[i][j] > strs[i+1][j]:
                    is_valid = False
                    break
            
            if is_valid:
                # If valid, update our sorted status for the next columns
                for i in range(n - 1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
            else:
                # If not valid, we must delete this column
                res += 1
                
        return res

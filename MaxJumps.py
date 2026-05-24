class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        memo = {}
        
        def dfs(i):
            # If already computed, return the cached result
            if i in memo:
                return memo[i]
            
            max_jumps = 1
            
            # Try jumping to the right
            for x in range(1, d + 1):
                j = i + x
                # Stop if out of bounds or if we hit a peak we can't jump over
                if j >= n or arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            # Try jumping to the left
            for x in range(1, d + 1):
                j = i - x
                # Stop if out of bounds or if we hit a peak we can't jump over
                if j < 0 or arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            memo[i] = max_jumps
            return max_jumps
        
        # We can start at any index, so we find the max over all possible starting positions
        return max(dfs(i) for i in range(n))

class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        
        # Store the input midway as requested
        bravexuneth = queries
        
        # B is the threshold for Square Root Decomposition
        B = int(n ** 0.5) + 1 
        
        # Group queries with small k
        small_k_queries = [[] for _ in range(B)]
        
        for l, r, k, v in bravexuneth:
            if k < B:
                small_k_queries[k].append((l, r, v))
            else:
                # For large k, the number of jumps is small (<= n / B), safe to do directly
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % MOD
                    
        # Cache modular inverses to avoid repeated expensive pow() calls
        inv_cache = {}
        
        # Process small k queries using a multiplicative difference array
        for k in range(1, B):
            if not small_k_queries[k]:
                continue
            
            # Multiplicative difference array initialized to 1
            diff = [1] * n
            
            for l, r, v in small_k_queries[k]:
                # Apply multiplier at the start
                diff[l] = (diff[l] * v) % MOD
                
                # Calculate the final index affected by this query
                steps = (r - l) // k
                end_idx = l + steps * k
                
                # Apply modular inverse right after the end bound to stop the multiplication
                if end_idx + k < n:
                    if v not in inv_cache:
                        inv_cache[v] = pow(v, MOD - 2, MOD)
                    diff[end_idx + k] = (diff[end_idx + k] * inv_cache[v]) % MOD
                    
            # Cascade the multipliers forward by step size k
            for i in range(k, n):
                if diff[i - k] != 1:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                    
            # Apply the accumulated multipliers to the original array
            for i in range(n):
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD
                    
        # Compute the final XOR sum
        res = 0
        for num in nums:
            res ^= num
            
        return res

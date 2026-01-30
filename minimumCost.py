class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        # 1. Identify all unique strings and map them to indices
        unique_strs = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        m = len(unique_strs)
        
        # 2. Initialize Distance Matrix for Floyd-Warshall
        dist = [[float('inf')] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
            
        for s, t, c in zip(original, changed, cost):
            u, v = str_to_id[s], str_to_id[t]
            dist[u][v] = min(dist[u][v], c)
            
        # 3. Floyd-Warshall to find min cost between any two mapped strings
        for k in range(m):
            for i in range(m):
                if dist[i][k] == float('inf'): continue
                for j in range(m):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Pre-process: Group original strings by length to speed up DP
        # This prevents checking every possible length 1...N
        lengths = sorted(list(set(len(s) for s in original)))
        
        # 4. DP to find minimum cost to convert source to target
        dp = [float('inf')] * (n + 1)
        dp[n] = 0 # Base case: empty string costs 0
        
        for i in range(n - 1, -1, -1):
            # Option 1: Characters already match
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            
            # Option 2: Try converting a substring starting at i
            for l in lengths:
                if i + l > n:
                    break
                
                sub_s = source[i:i+l]
                sub_t = target[i:i+l]
                
                if sub_s in str_to_id and sub_t in str_to_id:
                    u, v = str_to_id[sub_s], str_to_id[sub_t]
                    if dist[u][v] != float('inf'):
                        dp[i] = min(dp[i], dist[u][v] + dp[i + l])
                        
        return dp[0] if dp[0] != float('inf') else -1

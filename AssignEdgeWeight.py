from collections import deque

class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 18 # Since 2^17 = 131072 > 10^5
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # Step 1: BFS to find the depth of each node and its direct parent
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr  # 2^0 = 1st parent
                    queue.append(neighbor)
                    
        # Step 2: Populate the binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                # The 2^j-th parent is the 2^(j-1)-th parent of the 2^(j-1)-th parent
                up[i][j] = up[up[i][j-1]][j-1]
                
        # Helper function to find the Lowest Common Ancestor
        def get_lca(u, v):
            # Ensure u is deeper than v
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring u up to the same depth as v
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both u and v up until we find the LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]
            
        # Step 3: Precompute powers of 2 to handle modulos in O(1) time
        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        # Step 4: Answer each query
        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[lca]
            
            if d == 0:
                ans.append(0)
            else:
                ans.append(pow2[d - 1])
                
        return ans


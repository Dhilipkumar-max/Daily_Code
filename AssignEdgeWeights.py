class Solution(object):
    def assignEdgeWeights(self, edges):
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS to find the maximum depth
        q = [1]
        visited = [False] * (n + 1)
        visited[1] = True
        max_depth = -1
        
        while q:
            nxt = []
            for u in q:
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        nxt.append(v)
            q = nxt
            max_depth += 1  # Increment depth for each level processed
            
        MOD = 10**9 + 7
        
        # Calculate 2^(L-1) modulo 10^9 + 7
        return pow(2, max_depth - 1, MOD)


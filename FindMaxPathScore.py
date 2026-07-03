from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        unique_costs = set()
        
        # 1. Build the graph using only online nodes
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                unique_costs.add(cost)
                
        # If there are no valid edges available at all
        if not unique_costs:
            return -1
            
        unique_costs = sorted(list(unique_costs))
        
        # 2. Compute Topological Sort (Kahn's Algorithm)
        q = deque()
        for i in range(n):
            if online[i] and in_degree[i] == 0:
                q.append(i)
                
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        INF = 10**18
        
        # 3. Validation function for binary search
        def check(min_cost):
            dist = [INF] * n
            dist[0] = 0
            
            # Process nodes in topological order to find shortest paths
            for u in topo:
                if u == n - 1:
                    # n - 1 is fully evaluated once we reach it in topo sort
                    break
                
                d_u = dist[u]
                if d_u != INF:
                    for v, cost in adj[u]:
                        if cost >= min_cost:
                            if d_u + cost < dist[v]:
                                dist[v] = d_u + cost
                                
            return dist[n-1] <= k

        # 4. Binary search over sorted unique edge costs
        low = 0
        high = len(unique_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(unique_costs[mid]):
                ans = unique_costs[mid]
                # Try to look for a higher minimum cost score
                low = mid + 1
            else:
                # The path is either disconnected or costs more than k
                high = mid - 1
                
        return ans


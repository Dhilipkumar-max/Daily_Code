class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        base_parent = list(range(n))
        
        # Iterative path compression to avoid deep recursion
        def find(i, parent):
            root = i
            while root != parent[root]:
                root = parent[root]
            curr = i
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
            return root

        def union(i, j, parent):
            root_i = find(i, parent)
            root_j = find(j, parent)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        base_comps = n
        min_must = float('inf')
        optional_edges = []
        
        # 1. Process Mandatory Edges
        for u, v, s, must in edges:
            if must == 1:
                # If a mandatory edge forms a cycle, a valid spanning tree is impossible
                if union(u, v, base_parent):
                    base_comps -= 1
                    min_must = min(min_must, s)
                else:
                    return -1
            else:
                optional_edges.append((u, v, s))
                
        # 2. Quick pre-check: Is it even possible to connect the graph at all?
        test_parent = base_parent[:]
        test_comps = base_comps
        max_opt = 0
        for u, v, s in optional_edges:
            if union(u, v, test_parent):
                test_comps -= 1
            if s > max_opt:
                max_opt = s
                
        # If we used every possible edge and it's still disconnected
        if test_comps > 1:
            return -1
            
        # 3. Binary Search Setup
        # Max theoretical stability is bound by our weakest mandatory edge.
        # If there are no mandatory edges, it is bound by 2 * the strongest optional edge.
        high = min_must if min_must != float('inf') else 2 * max_opt
        low = 1
        ans = -1
        
        def can(X):
            """Returns True if we can form a spanning tree with stability >= X using <= k upgrades"""
            parent = base_parent[:]
            comps = base_comps
            upgrades = 0
            
            # Pass 1: Add edges that don't need upgrades (strength >= X)
            for u, v, s in optional_edges:
                if s >= X:
                    if union(u, v, parent):
                        comps -= 1
            
            if comps == 1:
                return True
                
            # Pass 2: Add edges that need exactly 1 upgrade (strength < X <= 2 * strength)
            for u, v, s in optional_edges:
                if s < X and 2 * s >= X:
                    if union(u, v, parent):
                        comps -= 1
                        upgrades += 1
                        if comps == 1:
                            break
                            
            return comps == 1 and upgrades <= k

        # 4. Execute Binary Search
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1  # Try for a higher stability
            else:
                high = mid - 1 # Stability is too high, lower it
                
        return ans

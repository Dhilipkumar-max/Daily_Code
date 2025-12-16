class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        # Build adjacency list for the tree
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)

        # Helper to merge two knapsack DP arrays
        # dp1: accumulated results so far
        # dp2: results from a new child
        def merge(dp1, dp2):
            new_dp = [-float('inf')] * (budget + 1)
            # Optimization: Only iterate over reachable states
            # Get indices where dp1 is valid
            valid_c1 = [c for c, val in enumerate(dp1) if val != -float('inf')]
            
            for c1 in valid_c1:
                val1 = dp1[c1]
                # We can stop early if c1 + c2 > budget, so range is limited
                limit = budget - c1 + 1
                for c2 in range(limit):
                    if dp2[c2] != -float('inf'):
                        if val1 + dp2[c2] > new_dp[c1 + c2]:
                            new_dp[c1 + c2] = val1 + dp2[c2]
            return new_dp

        def dfs(u):
            # Aggregates for children
            # agg_with_disc: Combined best of children if u IS bought (children get discount)
            # agg_no_disc: Combined best of children if u is NOT bought (children full price)
            
            # Initialize with 0 cost = 0 profit
            agg_with_disc = [-float('inf')] * (budget + 1)
            agg_with_disc[0] = 0
            
            agg_no_disc = [-float('inf')] * (budget + 1)
            agg_no_disc[0] = 0
            
            # Process all children
            for v in adj[u]:
                child_bought, child_not_bought = dfs(v)
                
                # If u is bought, children see "parent bought" -> use child_bought
                agg_with_disc = merge(agg_with_disc, child_bought)
                
                # If u is NOT bought, children see "parent not bought" -> use child_not_bought
                agg_no_disc = merge(agg_no_disc, child_not_bought)
            
            # Prepare result arrays for node u
            # res_parent_bought: Best for subtree u if u's parent bought
            # res_parent_not_bought: Best for subtree u if u's parent didn't buy
            res_parent_bought = [-float('inf')] * (budget + 1)
            res_parent_not_bought = [-float('inf')] * (budget + 1)
            
            # Costs and Profits for node u
            idx = u - 1
            cost_full = present[idx]
            cost_disc = present[idx] // 2
            profit_full = future[idx] - cost_full
            profit_disc = future[idx] - cost_disc
            
            # 1. Calculate res_parent_bought
            # Scenario A: We Buy u (Cost: cost_disc).
            # If we buy u, children get discount -> use agg_with_disc
            for c in range(cost_disc, budget + 1):
                if agg_with_disc[c - cost_disc] != -float('inf'):
                    res_parent_bought[c] = max(res_parent_bought[c], 
                                               agg_with_disc[c - cost_disc] + profit_disc)
            
            # Scenario B: We Skip u (Cost: 0).
            # If we skip u, children don't get discount -> use agg_no_disc
            for c in range(budget + 1):
                if agg_no_disc[c] != -float('inf'):
                    res_parent_bought[c] = max(res_parent_bought[c], agg_no_disc[c])
                    
            # 2. Calculate res_parent_not_bought
            # Scenario A: We Buy u (Cost: cost_full).
            # Children get discount -> use agg_with_disc
            for c in range(cost_full, budget + 1):
                if agg_with_disc[c - cost_full] != -float('inf'):
                    res_parent_not_bought[c] = max(res_parent_not_bought[c], 
                                                   agg_with_disc[c - cost_full] + profit_full)
            
            # Scenario B: We Skip u (Cost: 0).
            # Children don't get discount -> use agg_no_disc
            for c in range(budget + 1):
                if agg_no_disc[c] != -float('inf'):
                    res_parent_not_bought[c] = max(res_parent_not_bought[c], agg_no_disc[c])
            
            return res_parent_bought, res_parent_not_bought

        # Root is 1. CEO has no boss, so "parent not bought" applies (full price).
        _, root_res = dfs(1)
        
        # Result is the max profit achievable within budget
        return max(0, max(root_res))

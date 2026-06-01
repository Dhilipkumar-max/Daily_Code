class Solution(object):
    def minimumCost(self, cost):
        # Sort the costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate over the sorted costs
        for i in range(len(cost)):
            # Every 3rd candy (index 2, 5, 8...) is free
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost


class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Array to hold the component ID for each node
        component_id = [0] * n
        current_id = 0
        
        # Build the connected components
        for i in range(1, n):
            # If the difference between adjacent elements exceeds maxDiff, 
            # they cannot be connected. Start a new component.
            if nums[i] - nums[i - 1] > maxDiff:
                current_id += 1
            
            component_id[i] = current_id
            
        # Answer each query by checking if both nodes belong to the same component
        return [component_id[u] == component_id[v] for u, v in queries]

from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge case: If the array has only 1 element, we are already at the end.
        if n <= 1:
            return 0
            
        # Map each value to a list of its indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # Initialize BFS queue and visited set
        # queue stores tuples of (current_index, steps_taken)
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            node, steps = queue.popleft()
            
            # If we reach the last index, return the number of steps
            if node == n - 1:
                return steps
                
            val = arr[node]
            
            # Explore all 3 types of jumps:
            
            # 1. Jump to indices with the same value
            for neighbor in graph[val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
            
            # CRITICAL OPTIMIZATION: Clear the list for this value to prevent 
            # redundant processing and avoid O(N^2) time complexity.
            graph[val] = []
            
            # 2 & 3. Jump to adjacent indices (i - 1, i + 1)
            for neighbor in (node - 1, node + 1):
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
                    
        return -1

from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # Initialize a queue for BFS and a set to keep track of visited indices
        queue = deque([start])
        visited = {start}
        
        while queue:
            curr = queue.popleft()
            
            # Check if we reached the target value
            if arr[curr] == 0:
                return True
            
            # Explore both possible jump directions
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                # Ensure the jump is within bounds and the index hasn't been visited yet
                if 0 <= next_idx < len(arr) and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append(next_idx)
                    
        return False

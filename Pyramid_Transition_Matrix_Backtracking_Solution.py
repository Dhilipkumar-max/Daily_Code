from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # Map the bottom pair to possible top blocks
        # e.g., "AB" -> ["C", "D"]
        adj = defaultdict(list)
        for triple in allowed:
            adj[triple[:2]].append(triple[2])
            
        memo = {}

        def solve(current_row, next_row):
            # If the current row is length 1, we reached the top
            if len(current_row) == 1:
                return True
            
            # If we finished building the next row, move up a level
            if len(next_row) == len(current_row) - 1:
                return solve(next_row, "")
            
            # State for memoization: current row and progress on the next row
            state = (current_row, next_row)
            if state in memo:
                return memo[state]
            
            # Determine which pair we are currently looking at
            i = len(next_row)
            base_pair = current_row[i:i+2]
            
            # Try all allowed blocks for this pair
            if base_pair in adj:
                for top in adj[base_pair]:
                    if solve(current_row, next_row + top):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return False

        return solve(bottom, "")

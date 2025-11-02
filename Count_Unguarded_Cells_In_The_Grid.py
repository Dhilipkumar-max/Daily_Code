class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        guards_set = set((r, c) for r, c in guards)
        walls_set = set((r, c) for r, c in walls)
        guarded = set()
        
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and (nr, nc) not in walls_set and (nr, nc) not in guards_set:
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc
        
        # Count unguarded cells
        total_cells = m * n
        occupied = len(guards_set) + len(walls_set) + len(guarded)
        return total_cells - occupied

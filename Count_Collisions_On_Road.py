class Solution(object):
    def countCollisions(self, directions):
        i, n = 0, len(directions)
        # Skip all leading L
        while i < n and directions[i] == 'L':
            i += 1
        j = n - 1
        # Skip all trailing R
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # Count all remaining moving cars (L or R)
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
        return collisions

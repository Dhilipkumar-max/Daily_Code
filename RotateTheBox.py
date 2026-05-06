class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # Step 1: Simulate gravity by letting stones fall to the right
        for i in range(m):
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    # Obstacle blocks the way; next available spot is to its left
                    empty_pos = j - 1
                elif boxGrid[i][j] == '#':
                    # Move stone to the furthest right empty position
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty_pos] = '#'
                    empty_pos -= 1
                    
        # Step 2: Rotate the grid 90 degrees clockwise
        rotated_box = [['.'] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = boxGrid[i][j]
                
        return rotated_box

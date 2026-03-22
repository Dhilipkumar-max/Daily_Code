class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        # Check all 4 possible rotations (0, 90, 180, 270 degrees)
        for _ in range(4):
            if mat == target:
                return True
            # Rotate the matrix 90 degrees clockwise
            mat = [list(x) for x in zip(*mat[::-1])]
            
        return False

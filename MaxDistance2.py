class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        # If ends have different colors, maximum distance is n-1
        if colors[0] != colors[n-1]:
            return n - 1
        
        # Ends have same color, find max distance to a different color house
        # From left: farthest house with different color
        max_dist = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
        
        # From right: farthest house with different color
        for i in range(n):
            if colors[i] != colors[n-1]:
                max_dist = max(max_dist, n - 1 - i)
                break
        
        return max_dist

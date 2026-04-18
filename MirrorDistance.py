class Solution(object):
    def mirrorDistance(self, n):
        
        reversed_n = int(str(n)[::-1])
        
        return abs(n - reversed_n)

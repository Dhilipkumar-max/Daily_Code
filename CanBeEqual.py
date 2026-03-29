class Solution(object):
    def canBeEqual(self, s1, s2):
        # Group characters by parity of their indices
        # Even positions: index 0 and 2
        # Odd positions: index 1 and 3
        
        # Check even indices
        even1 = sorted([s1[0], s1[2]])
        even2 = sorted([s2[0], s2[2]])
        
        # Check odd indices
        odd1 = sorted([s1[1], s1[3]])
        odd2 = sorted([s2[1], s2[3]])
        
        return even1 == even2 and odd1 == odd2

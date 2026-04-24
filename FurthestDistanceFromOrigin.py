class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_wildcard = moves.count('_')
        
        return abs(count_L - count_R) + count_wildcard
        

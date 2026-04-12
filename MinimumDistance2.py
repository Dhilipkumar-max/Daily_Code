class Solution(object):
    def minimumDistance(self, word):
        def get_dist(char1, char2):
            if char1 is None: return 0
            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
        dp = {26: 0} 
        
        for i in range(len(word)):
            new_dp = {}
            curr_char = word[i]
            prev_char = word[i-1] if i > 0 else None
            
            for other_pos, dist in dp.items():
                other_char = chr(ord('A') + other_pos) if other_pos < 26 else None
                d1 = dist + get_dist(prev_char, curr_char)
                new_dp[other_pos] = min(new_dp.get(other_pos, float('inf')), d1)
                d2 = dist + get_dist(other_char, curr_char)
                prev_idx = ord(prev_char) - ord('A') if prev_char else 26
                new_dp[prev_idx] = min(new_dp.get(prev_idx, float('inf')), d2)
                
            dp = new_dp
            
        return min(dp.values())

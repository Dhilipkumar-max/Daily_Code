class Solution(object):
    def minFlips(self, s):
        n = len(s)
        # Double the string to simulate all possible rotations
        s = s + s
        
        # Create the two target alternating patterns
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"
        
        res = float('inf')
        diff1, diff2 = 0, 0
        l = 0
        
        for r in range(len(s)):
            # Add the current character's difference to the counts
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1
            
            # Once the window reaches size n
            if (r - l + 1) > n:
                # Remove the leftmost character's contribution
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                l += 1
            
            # If the window is exactly size n, track the minimum flips
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
                
        return res

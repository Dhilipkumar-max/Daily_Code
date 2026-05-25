class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        # dp[i] will be True if index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # count tracks how many reachable indices are in the current window [i - maxJump, i - minJump]
        count = 0
        
        for i in range(1, n):
            # As we move i, we need to maintain the window [i - maxJump, i - minJump]
            # Add the index that just entered the window
            if i >= minJump:
                if dp[i - minJump]:
                    count += 1
            
            # Remove the index that just left the window
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    count -= 1
            
            # If s[i] is '0' and there is at least one reachable index in range, i is reachable
            if s[i] == '0' and count > 0:
                dp[i] = True
                
        return dp[n - 1]

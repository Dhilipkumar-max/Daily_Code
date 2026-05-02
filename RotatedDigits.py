class Solution(object):
    def rotatedDigits(self, n):
        count = 0
        
        for i in range(1, n + 1):
            num_str = str(i)
            
            # Condition 1: The number cannot contain any invalid digits
            if '3' in num_str or '4' in num_str or '7' in num_str:
                continue
                
            # Condition 2: The number must contain at least one digit that changes its value
            if '2' in num_str or '5' in num_str or '6' in num_str or '9' in num_str:
                count += 1
                
        return count

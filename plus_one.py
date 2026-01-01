class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Iterate from the last element to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is less than 9, just add 1 and we are done
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and we continue the loop
            digits[i] = 0
        
        # If we exit the loop, it means all digits were 9 (e.g., 999 -> 000)
        # We need to add a 1 at the front
        return [1] + digits

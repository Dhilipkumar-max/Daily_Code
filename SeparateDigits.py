class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        
        for num in nums:
            # Convert the number to a string to iterate over digits
            for digit in str(num):
                # Convert character back to int and add to result
                answer.append(int(digit))
                
        return answer

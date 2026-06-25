from collections import defaultdict

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Dictionary to store frequencies of prefix sums
        freq = defaultdict(int)
        
        # Base case: Before parsing any elements, the prefix sum is 0
        freq[0] = 1
        
        curr_sum = 0
        smaller_count = 0
        ans = 0
        
        for num in nums:
            if num == target:
                # If curr_sum is about to increase by 1, the number of previous 
                # prefix sums smaller than the *new* curr_sum increases by the 
                # count of the *old* curr_sum.
                smaller_count += freq[curr_sum]
                curr_sum += 1
            else:
                # If curr_sum decreases by 1, the number of previous prefix sums 
                # smaller than the *new* curr_sum decreases by the count of the 
                # *new* curr_sum.
                curr_sum -= 1
                smaller_count -= freq[curr_sum]
                
            # Add the valid starting positions to our answer
            ans += smaller_count
            
            # Record the current prefix sum in our frequency tracker
            freq[curr_sum] += 1
            
        return ans

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG = -10**15  # a very small integer instead of -inf
        dp = [0, NEG, NEG]

        for num in nums:
            new_dp = dp[:]  
            for r in range(3):
                if dp[r] != NEG:  # ensure valid state
                    new_sum = dp[r] + num
                    new_dp[new_sum % 3] = max(new_dp[new_sum % 3], new_sum)
            dp = new_dp

        return dp[0]

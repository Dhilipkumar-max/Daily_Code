class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

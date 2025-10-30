class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        operations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        return operations

if __name__ == "__main__":
    sol = Solution()
    target = [1, 2, 3, 2, 1]
    result = sol.minNumberOperations(target)
    print("Minimum number of operations:", result)

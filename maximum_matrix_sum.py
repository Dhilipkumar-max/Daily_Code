class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.subtree_sums = []
        
        # Helper function to calculate subtree sums
        def calculate_sum(node):
            if not node:
                return 0
            
            # Post-order: sum of current node = val + left_sum + right_sum
            current_sum = node.val + calculate_sum(node.left) + calculate_sum(node.right)
            
            # Store this sum to evaluate later
            self.subtree_sums.append(current_sum)
            return current_sum
        
        # Step 1: Find total sum (which is the result of calculate_sum on root)
        total_sum = calculate_sum(root)
        
        # Step 2: Iterate through all recorded subtree sums to find max product
        max_prod = 0
        for s in self.subtree_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        # Step 3: Return modulo 10^9 + 7
        return max_prod % (10**9 + 7)

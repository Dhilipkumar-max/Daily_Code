class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Helper function returns (depth, candidate_node)
        def postOrder(node):
            if not node:
                return 0, None
            
            left_depth, left_node = postOrder(node.left)
            right_depth, right_node = postOrder(node.right)
            
            # Case 1: Left side is deeper. The deepest nodes are all on the left.
            if left_depth > right_depth:
                return left_depth + 1, left_node
            
            # Case 2: Right side is deeper. The deepest nodes are all on the right.
            elif right_depth > left_depth:
                return right_depth + 1, right_node
            
            # Case 3: Depths are equal. This node is the current LCA for the 
            # deepest nodes found in its subtrees.
            else:
                return left_depth + 1, node

        return postOrder(root)[1]

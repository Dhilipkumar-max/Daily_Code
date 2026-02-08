class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return checkHeight(root) != -1;
    }

private:
    int checkHeight(TreeNode* node) {
        if (node == nullptr) return 0;

        int leftHeight = checkHeight(node->left);
        if (leftHeight == -1) return -1;

        int rightHeight = checkHeight(node->right);
        if (rightHeight == -1) return -1;

        if (abs(leftHeight - rightHeight) > 1) {
            return -1;
        }

        return max(leftHeight, rightHeight) + 1;
    }
};

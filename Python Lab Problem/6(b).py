class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None 
class BST: 
    def __init__(self): 
        self.root = None 
    def insert(self, root, key): 
        if not root: 
            return Node(key) 
        if key < root.key: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
        return root 
    def printInorder(self, root): 
        if root: 
            self.printInorder(root.left) 
            print(root.key, end=" ") 
            self.printInorder(root.right) 
arr = list(map(int, input("Enter N positive integers separated by space: ").split())) 
bst = BST() 
root = None 
for num in arr: 
    root = bst.insert(root, num) 
print("Inorder Traversal of BST:") 
bst.printInorder(root) 
print()

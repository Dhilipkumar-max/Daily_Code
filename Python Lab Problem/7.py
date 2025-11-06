class AVLNode: 
    def __init__(self, key): 
        self.key = key 
        self.left = self.right = None 
        self.height = 1 
class AVLTree: 
    def insert(self, root, key): 
        if not root: 
            return AVLNode(key) 
        if key < root.key: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
        balance = self.getBalance(root) 
        if balance > 1 and key < root.left.key: 
            return self.rightRotate(root) 
        if balance < -1 and key > root.right.key: 
            return self.leftRotate(root) 
        if balance > 1 and key > root.left.key: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        if balance < -1 and key < root.right.key: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        return root 
    def getHeight(self, node): 
        return node.height if node else 0 
    def getBalance(self, node): 
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0 
    def leftRotate(self, z): 
        y = z.right 
        T2 = y.left 
        y.left = z 
        z.right = T2 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 
    def rightRotate(self, y): 
        x = y.left 
        T2 = x.right 
        x.right = y 
        y.left = T2 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right)) 
        return x 
    def inorder(self, root): 
        if root: 
            self.inorder(root.left) 
            print(root.key, end=" ") 
            self.inorder(root.right)  
avl = AVLTree() 
root = None 
keys = [10, 20, 30, 15, 50, 25]  # Sample input 
for key in keys: 
    root = avl.insert(root, key) 
print("Inorder Traversal of Balanced AVL Tree:") 
avl.inorder(root)

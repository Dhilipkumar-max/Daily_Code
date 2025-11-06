class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left = self.right = None 

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

    def search(self, root, key): 
        if not root or root.key == key: 
            return root 
        return self.search(root.left, key) if key < root.key else self.search(root.right, key) 

    def inorder(self, root): 
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

bst = BST()  
root = None  
elements = [50, 30, 70, 20, 40, 60, 80]  
for key in elements:  
    root = bst.insert(root, key)  

print("Inorder Traversal of BST:")  
bst.inorder(root)  
print()  

search_keys = [40, 100]  
for key in search_keys:  
    result = bst.search(root, key)  
    if result:  
        print(f"Search {key}: Found")  
    else:  
        print(f"Search {key}: Not Found")

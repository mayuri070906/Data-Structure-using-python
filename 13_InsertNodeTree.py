class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertBST(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insertBST(root.left, key)
    elif key > root.val:
        root.right = insertBST(root.right, key)

    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
    

# ---- DRIVER CODE ----
root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    root = insertBST(root, val)   # IMPORTANT

print("Inorder Traversal:")
inorder(root)
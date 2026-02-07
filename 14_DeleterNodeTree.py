class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insertBST(root,key):
    if root is None:
        return TreeNode(key)
    
    if key<root.val:
        root.left=insertBST(root.left,key)
    elif key>root.val:
        root.right=insertBST(root.right,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def minValueNode(root):
    current=root
    while current.left:
        current=current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root

    if key < root.val:
        root.left=deleteNode(root.left,key)
    elif key > root.val:
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp=minValueNode(root.right)
        root.val=temp.val
        root.right=deleteNode(root.right,temp.val)
    return root
    
root = None
n=int(input("enter number of nodes::"))

for i in range(n):
    val=int(input(f"enter value{i+1}::"))
    root=insertBST(root,val)

print("inorder travarsal before deletion::")
inorder(root)

key=int(input("Enter value to delete::"))
root=deleteNode(root,key)

print("inorder travarsal after deletion::")
inorder(root)



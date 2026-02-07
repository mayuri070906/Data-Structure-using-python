class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insertBST(root,val):
    if root is None:
        return TreeNode(val)
    
    if val<root.val:
        root.left=insertBST(root.left,val)
    
    elif val>root.val:
        root.right=insertBST(root.right,val)

    return root

def isvalidBST(root):
    def check(node,min,max):
        if not node:
            return True
        if node.val <= min or node.val >= max:
            return False
        
        return (check(node.left, min, node.val) and
                check(node.right, node.val, max))
    return check(root,float('-inf'),float('inf'))

root=None
n=int(input("enter number of node::"))

for i in range(n):
    val=int(input(f"enter value {i+1}::"))
    root=insertBST(root,val)

if isvalidBST(root):
    print("valid BST")
else:
    print("Invalid BST")


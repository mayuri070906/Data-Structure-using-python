class AVLNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1
    
class AVLTree:
    def get_height(self,node):
        if not None:
            return 0
        return node.height

    def get_balance(self,node):
        if not None:
            return 0
        return self.get_height(node.left)-self.get_height(node.right)
    
    def right_rotate(self,y):
        x=y.left
        T2=x.right

        x.right=y
        y.left=T2

        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        return x

    def left_rotate(self,x):
        y=x.right
        T2=y.left

        y.left=x
        x.right=T2

        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
        return y

    def insert(self,root,key):
        if root is None:
            return AVLNode(key)
        
        if key<root.key:
            root.left=self.insert(root.left,key)

        else:
            root.right=self.insert(root.right,key)

        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        balance=self.get_balance(root)

        # LL
        if balance>1 and key<root.left.key:
            return self.right_rotate(root)

        # RR
        if balance<-1 and key>root.right.key:
            return self.left_rotate(root)

        # LR
        if balance>1 and key>root.right.key:
            root_left=self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance<-1 and key<root.left.key:
            root_right=self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end=" ")
            self.inorder(root.right)

avl=AVLTree()
root=None
n=int(input("enter value of Node:"))
for i in range(n):
    value=int(input(f"enter value {i+1}::"))
    root=avl.insert(root,value)

print("\n Inorder traversal of AVL tree::")
avl.inorder(root)



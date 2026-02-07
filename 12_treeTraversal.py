class Node:
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None


def create():
    ch = int(input("\nPress 1 to create node, 0 to not create: "))
    
    if ch == 0:
        return None
    else:
        data = int(input("Enter data: "))
        newnode = Node(data)

        print(f"Do you want to add node to LEFT of {data}?")
        newnode.llink = create()

        print(f"Do you want to add node to RIGHT of {data}?")
        newnode.rlink = create()

        return newnode


def inorder(root):
    if root is not None:
        inorder(root.llink)
        print(root.data, end=" ")
        inorder(root.rlink)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.llink)
        preorder(root.rlink)


def postorder(root):
    if root is not None:
        postorder(root.llink)
        postorder(root.rlink)
        print(root.data, end=" ")


# -------- Main --------
root = None
root = create()

if root is None:
    print("\nTree is empty")
else:
    print("\nInorder Traversal:")
    inorder(root)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nPostorder Traversal:")
    postorder(root)

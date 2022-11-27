class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None

#INORDER TRAVERSAL

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end="  ")
        inorder(root.right)

#PRE-ORDER TRSVERSE

def preorder(root):
    if root==None:
        return -1
    print(root.data,end="  ")
    preorder(root.left)
    preorder(root.right)

#POST ORDER TRAVERSE

def postorder(root):
    if root==None:
        return -1
    postorder(root.left)
    postorder(root.right)
    print(root.data, end="  ")


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(6)
    root.left.right = Node(9)

    print("\nIntorder traversal of binary tree is")
    inorder(root)
    print("\n\nPretorder traversal of binary tree is")
    preorder(root)
    print("\n\nPostorder traversal of binary tree is")
    postorder(root)
    

 



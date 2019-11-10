# Sum of nodes in bottom view of Binary Tree
#  Nodes that are visible when tree is seen from bottom.
#             6
#          5    10
#        2         12
#      1         11    16
#    0
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def sum():
    pass

def insert(root,key):
    if root is None:
        return(Node(key))
    else:
        if key <= root.data:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
        return root

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

if __name__=='__main__':
    root=None
    root=insert(root,1)
    insert(root,2)
    insert(root,3)
    insert(root,4)
    insert(root,5)
    insert(root,6)

    inorder(root)
#  A program to make Binary tree
#  And then
# Find the node with minimum value
# in a Binary Search Tree

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def insert(root,key):

    if root is None:
        return(Node(key))
    else:
        if key <= root.data:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
        return root

def min_value(root):

    """
    current =root
    while(current.left is not None):
        current= current.left
    return current.data
    """
    # by using recursive function
    if root.left == None:
        return root.data
    return min_value(root.left)



def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

if __name__=='__main__':
    root=None
    root=insert(root,5)
    insert(root,2)
    insert(root,7)
    insert(root,6)
    insert(root,1)
    insert(root,4)
    inorder(root)
    print()
    print("min value is ",min_value(root))

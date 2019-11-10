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
            root.left= insert(root.left,key)
        else:
            root.right = insert(root.right,key)
        return root

def inorder(root):
    if (not root):
        return

    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def max(root):
    if root.right is None:
        return root.data
    return max(root.right)

if __name__=='__main__':
    root=None
    root=insert(root,10)
    insert(root,5)
    insert(root,11)
    insert(root,50)
    insert(root,15)
    insert(root,1)
    insert(root,2)

    inorder(root)
    max_value = max(root)
    print("Max Value in BT is : %s" %max_value)
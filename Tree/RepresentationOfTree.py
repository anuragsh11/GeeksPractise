#              10
#          8       12
#       6    9   11   14
#
#
#
#
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left = None

def inorder(temp):
    if(not temp):
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

def insert(root,data):
    q=[]
    q.append(root)
    print(len(q))
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if (not temp.left):
            temp.left=Node(data)
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right=Node(data)
            break
        else:
            q.append(temp.right)


if __name__=='__main__':
    root=Node(10)
    root.left=Node(8)
    root.right=Node(12)
    root.left.left=Node(6)
    root.left.right=Node(9)
    root.right.left=Node(11)
    root.right.right=Node(14)

    print("in order traversal of list" ,end=" ")
    inorder(root)
    print("inserting element")
    insert(root,7)
    inorder(root)


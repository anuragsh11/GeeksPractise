# Remove last node of the linked list
# Given a linked list, the task is to remove the last node of the
# linked list and update the head pointer of the linked list.


class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head=new_node

    def delete_node(self,delete_node):
        pass

    if __name__ =='__main__':
        head =None

        head = push(12)
        head = push(29)
        head = push(11)
        head = push(23)
        head = push(8)

        #head = removeLastNode(head)
        while (head):
            print("{} ".format(head.data), end="")
            head = head.next

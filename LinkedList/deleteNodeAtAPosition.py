#
# Delete a Linked List node at a given position
#



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head= new_node
            return
        start= self.head
        while(start.next):
            start=start.next
        start.next=new_node

    def delete(self,position):
        if self.head == None:
            return
        temp=self.head
        if position == 0:
            temp=temp.next
            return
        for i in range(position):



    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

ll = LinkedList()
ll.append(2)
ll.append(3)
ll.append(21)
ll.append(32)
ll.append(29)
ll.append(7)
ll.print()
ll.delete(0)
print(" ")
ll.print()
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):
        new_node=Node(new_data)
        new_node.next = prev_node.next
        prev_node.next= new_node

    def append(self,new_data):
        new_node= Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last= self.head
        while(last.next):
            last =last.next
        last.next=new_node

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


ll=LinkedList()
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.append(5)
#print(ll.head.next)
ll.insertAfter(ll.head.next.next.next,6)
ll.print()

# Delete Nth node from the end of the given linked list
#
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
            self.head=new_node
            return

        start = self.head
        while (start.next):
            start = start.next
        start.next = new_node
    #1 3 4 22 11 2 33 4
    def delete_nth_element(self,n):
        pntr1 = self.head
        pntr2 = self.head

        for i in range(n):
            if pntr2.next == None :
                if (i == n - 1):
                    self.head = self.head.next
                return self.head
            pntr2=pntr2.next

        while(pntr2.next):
            pntr2=pntr2.next
            pntr1=pntr1.next
        #print(pntr1.data,pntr2.data)
        pntr1.next = pntr1.next.next


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
print("")
ll.delete_nth_element(7)
ll.print()
# write a program to create circular linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circle:
    def __init__(self):
        self.head=None

    def add(self,data):
        newNode=Node(data)
        temp=self.head
        newNode.next=self.head
        if self.head is not None:
            while(temp.next!=self.head):
                temp=temp.next

            temp.next=newNode
        else:
            newNode.next=newNode
        self.head=newNode
    def display(self):
        temp=self.head
        if self.head is  not None:
            while(True):
                print(temp.data,end=' ')
                temp=temp.next
                if (temp==self.head):
                    break
obj=Circle()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
print("Contents of circular linked list is",end=' ')
obj.display()
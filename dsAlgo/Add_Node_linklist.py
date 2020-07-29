# write a program to insert node in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
class Doublelink:
    def __init__(self):
        self.head=None
        self.tail=None
    def addAtstart(self,data):
        newNode =Node(data);
        if (self.head==None):
            self.head=self.tail=newNode
            self.head.previous=None
            self.tail.next=None

        else:
            self.head.previous=newNode
            newNode.next=self.head
            newNode.previous=None
            self.head=newNode

    def display(self):
        current=self.head
        if (self.head==None):
            print('list is empty')
            return
        print("Adding a node to the start of the list:")
        while(current!=None):
            print(current.data,end=' '),
            current = current.next
        print()

obj=Doublelink()
obj.addAtstart(1)
obj.display()
obj.addAtstart(2)
obj.display()
obj.addAtstart(4)
obj.display()
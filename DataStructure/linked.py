# write  a  program to implement linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data,end=' ')
            temp=temp.next
if __name__=="__main__":
    llist = Linklist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next =third
    llist.printlist()

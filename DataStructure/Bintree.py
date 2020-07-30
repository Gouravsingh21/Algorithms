#write a program to create a Binary tree
class BinTree:
    def __init__(self,key):
        self.root=key
        self.left=None
        self.right=None

    def add(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=BinTree(data)
                else:
                    self.left.add(data)
            if data>self.data:
                if self.right is None:
                    self.right=BinTree(data)
                else:
                    self.right.add(data)
    def display(self):
        if self.left:
            self.left.display()
        print(self.root,end=' '),
        if self.right:
            self.right.display()

root=BinTree(1)
root.left=BinTree(2)
root.right=BinTree(3)
root.left.left=BinTree(4)
root.right.right=BinTree(5)
root.display()
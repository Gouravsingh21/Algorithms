# write a python program to implement binary search tree

class Node:

    def __init__(self,data):
        self.data=data
        self.left =None
        self.right=None

    def addinto(self,data):
        if self.data:
            if self.data>data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.addinto(data)
            elif self.data<data:

                    if self.right is None:
                        self.right =Node(data)
                    else:
                        self.right.addinto(data)
            else:
                self.data=data

    def display(self):
        '''
        print('1 for inorder traversal \n 2 for preorder traversal \n 3 for post order traversal')
        n=int(input('enter your traversal choice'))
        '''
        if self.left:
            self.left.display()

        print(self.data)
        if self.right:
            self.right.display()



root=Node(12)
root.addinto(6)
root.addinto(14)
root.addinto(3)
root.addinto(7)
root.addinto(2)
root.display()





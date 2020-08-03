# write a program to create AVL TREE tree
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        self.height=1

class trees:
    def __init__(self):
        self.root=None
    def add(self,root,key):
        if root is None:
            #print('root makes')
            root=Node(key)
        else:
            if root.val>key:
                if root.left is None:

                    root.left=Node(key)
                else:

                    root.left=self.add(root.left,key)

            if root.val<key:
                if root.right is None:

                     root.right=Node(key)
                else:
                    root.right=self.add(root.right,key)
        # Step 2 to get height of parent node
        root.heigh=1 +max(self.height(root.left),self.height(root.right))

        # write a program to get balace factor
        balance=self.balance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def display(self,root):

        if not root:
            return
        self.display(root.left)
        print("{0} ".format(root.val), end="")
        #self.display(root.left)
        self.display(root.right)


    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y
    def height(self,root):
        if not root:
            return  0
        return root.height

    def balance(self,root):
        if not root:
            return 0
        return (self.height(root.left)-self.height(root.right))

    def preOrder(self, root):

        if not root:
            return
        print("{0} ".format(root.val),end='')
        self.preOrder(root.left)
        self.preOrder(root.right)




tree=trees()
root=None
root=tree.add(root,10)
root=tree.add(root,6)
root=tree.add(root,12)
root=tree.add(root,8)
root=tree.add(root,16)
root=tree.add(root,4)
root=tree.add(root,14)
root=tree.add(root,2)
print('inorder traversal',tree.display(root))
print('\n')
print('preorder traversal',tree.preOrder(root))
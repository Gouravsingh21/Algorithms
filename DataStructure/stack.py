# write a program to implement stack using list
class stack:
    #write constructer of the stack
    def __init__(self):
        self.container=[]
    #write push function to add new item in stack
    def push(self,data):
        self.container.append(data)
    #Write a function to deletes element from stack
    def pop(self):

        print(self.container.pop(len(self.container)-1),end=' ')
        print('removes',end=' ')
        print('\r')
    #Write a function to find the lenght of the given stack
    def size(self):
        count=0
        for i in self.container:
            count=count+1
        print(count)
    # write a function to display the peek of stack
    def peek(self):
        print(self.container[-1])
    #write a fucntion to display the stack
    def display(self):
        print('your  stack is',end=' ')
        lenght=len(self.container)
        for i in range(lenght-1,-1,-1):
            print(self.container[i],end=' ')
        print('\r')


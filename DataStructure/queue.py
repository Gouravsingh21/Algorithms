#write a python program to implement the queue
class Queue:
    def __init__(self):
        self.container=[]

    def enqueue(self,data):
        self.container.append(data)

    def dequeue(self):
        self.container.pop(0)

    def isempty(self):
        if self.container[len(self.container)-1]==None :
            print('True')
        else:
            print('False')

    def display(self):
        print('Your queue containes',end=' ')
        for i in range(0,len(self.container)):
            print(self.container[i],end=' ')
        print('\r')

obj=Queue()
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.display()
obj.dequeue()
obj.display()
obj.dequeue()
obj.display()
obj.isempty()
obj.dequeue()
obj.dequeue()
obj.isempty()
obj.display()
obj.isempty()
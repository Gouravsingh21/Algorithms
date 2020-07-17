#Write a code to implement binary search
class Binary:
    def __init__(self,lst,x,lst1):
        self.lst=lst
        self.x=x
        self.lst1=lst1
    def BinMethod(self):
        state=True
        a=0
        b = len(self.lst1)
        print('lenght of list',b)
        while (state):
            mid = (a + b) // 2
            if self.x>self.lst1[mid]:
                a=mid
            elif self.x<self.lst1[mid]:
                b=mid
            elif self.x==self.lst1[mid]:
                print('your index place',mid)
                state=False
                return mid
    def sorting(self):
        print('press 1 for sorted list input')
        print('press 2 for unsorted list input')
        n=int(input('enter your choice of input'))
        if n==1:
            self.lst1=eval(input('enter the sorted list'))
            self.x=int(input('enter the number you want to search'))
            obj.BinMethod()
        elif n==2:
            self.lst=eval(input('enter unsorted list'))
            self.x=int(input('enter the number you want to search'))
            a = len(self.lst)
            try:
                for i in range(0, a+1):
                    b = min(self.lst)
                    self.lst1.append(b)
                    self.lst.remove(b)
            except:
                pass
            finally:
                print('sorted list',self.lst1)
                obj.BinMethod()
        else:
            print('wrong input of choice')
        return ('process completing')
print('welcome to sorting and searching algorithm')
x=1
lst=[]
lst1=[]
obj=Binary(lst,x,lst1)
print(obj.sorting())




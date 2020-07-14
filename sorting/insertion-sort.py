# Write a python program to implement insertion sort
class Insertion:
    def __init__(self,lst):
        self.lst=lst
    def Method(self):
        for i in range (1,len(lst)):
            cur=lst[i]
            pos=i
            while cur<lst[pos-1] and pos>0:
                lst[pos]=lst[pos-1]
                pos=pos-1
            lst[pos]=cur
        print(lst)
lst=[4,1,0,9,3]
obj=Insertion(lst)
obj.Method()
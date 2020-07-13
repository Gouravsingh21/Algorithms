# Write a program to perform selection sort
class Selection:
    def __init__(self,lst):
        self.lst=lst
    def Method(self):
        for i in range(0,len(lst)-1):

            min_val=lst[i]
            for j in range (i+1,len(lst)):
                if min_val>lst[j]:
                    min_val,lst[j]=lst[j],min_val
                    lst[i]=min_val
        print(lst)


n=int(input('enter the number of element'))
lst=[int(input()) for i in range(0,n)]
obj=Selection(lst)
obj.Method()


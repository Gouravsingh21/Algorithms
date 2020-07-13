# Write a python program to implement bubble sort algorithm
class Bubble:
    def __init__(self,lst):
        self.lst=lst

    def Method(self):
        for i in range(0,len(lst)-1):
            for j in range(0, len(lst)-i-1):
                if lst[j]>lst[j+1]:
                    lst[j],lst[j+1]=lst[j+1],lst[j]
            print(lst)

lst=[64, 34, 25, 12, 22, 11, 90]
obj=Bubble(lst)
obj.Method()
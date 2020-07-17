#Write a program to perform quick sort
class Quick():
    def __init__(self,lst):
        self.lst=lst
    def Method(self):
        lenoflist=len(lst) #lenght of unsorted list
        pivot=lenoflist-1 #pivot element for comparison
        print('lenght of list',lenoflist)
        print('pivot element',lst[pivot])
        a=0 #variable define to stop left loop
        for left in range (0,len(lst)-1): # left loop for smaller comparison
            if a==1:
                break
            else:
                if lst[pivot]>lst[left]:
                    pass
                else:
                    for right in range(lenoflist-2,0,-1): #right loop for greater than comparison
                        if lst[left]==lst[right]:
                            lst[pivot],lst[right]=lst[right],lst[pivot]
                            print(lst)
                            a=1 #value of variable change to stop left loop
                            break
                        if lst[pivot]<lst[right]:
                            pass
                        else:
                            lst[left],lst[right]=lst[right],lst[left]
                            break #conditon to stop right loop and runs left loop





lst=[44,12,7,0,23,15,20,10,5,30,13]
obj=Quick(lst)
obj.Method()
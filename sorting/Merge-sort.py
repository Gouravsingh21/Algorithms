# Python program to implement merge sort
def divide(lst):
        if len(lst)>1:
            mid=len(lst)//2
            l=lst[:mid]
            r=lst[mid:]
            divide(l)
            divide(r)
            i=0
            j=0
            k=0
            while i<len(l) and j <len(r):
                if l[i]<r[j]:
                    lst[k]=l[i]
                    i=i+1
                    k=k+1
                else:
                    lst[k]=r[j]
                    j=j+1
                    k=k+1
            while i<len(l):
                lst[k]=l[i]
                i=i+1
                k=k+1
            while j<len(r):
                lst[k]=r[j]
                j=j+1
                k=k+1
lst=[44,12,7,0,23,15,20,10,5,30,13]
divide(lst)
print('sorted list',lst)

# write the program for quick-sort
def Method(lst,first,last):
    pivot=lst[first]
    left=first+1
    right=last
    while True:
        while left<=right and lst[left]<=pivot:
            left=left+1
        while left<=right and lst[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            lst[left],lst[right] = lst[right],lst[left]
    lst[first],lst[right]=lst[right],lst[first]
    return right
def run(lst,first,last):
    if first<last:
        p=Method(lst,first,last)
        run(lst,first,p-1)
        run(lst,p+1,last)
        print(lst)

lst=[44,12,7,0,23,15,20,10,5,30,13]
run(lst,0,len(lst)-1)
print(lst)
# Write a code to count the frequency of elements in the array
import array
class Count:
    def __init__(self,arr):
        self.arr=arr
    def Method(self):
        lenght=len(arr)
        show={}
        for index in range(0,len(arr)):
            count=0
            if str(arr[index]) in show:
                pass
            else:
                for j in range(index,len(arr)):

                    if arr[index]==arr[j]:
                        count=count+1
                        show[str(arr[index])]=count
                    else:
                        show[str(arr[index])]=count
        print('frequency dictionay is here',show)

arr=array.array('i',[1,2,1,2,3,4,5,1,2,9,10])
obj=Count(arr)
obj.Method()

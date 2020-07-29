#write a python program to rotate a array
import array as arr
def rotate(ar,n,ro):
    for i in range(0,n):
        first=ar[0]
        if i<ro:
            for j in range(1,n+1):
                ar[j-1]=ar[j]
                if j==n-1:
                    ar[n-1]=first
                    break
        else:
            break
    display(ar,n)
def display(ar,n):
    print('Rotated array',end=' ')
    for i in range(0,n):
        print(ar[i],end=' ')
    print('\r')
def main():
    a=arr.array('i',[1,2,3,4,5,6,7])
    print(a)
    n=len(a)
    #r=int(input('enter the no. of elements you wnat to rotate'))
    r=int(input('enter the no to rotate the array'))
    rotate(a,n,r)
main()

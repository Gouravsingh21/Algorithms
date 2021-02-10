# write a program to covert Float_binary to decimal

def point(num):
    num1=str(num)
    num1=list(num1)
    res=0
    count=0
    point_index=num1.index('.')

    # loop runs for the elements before point
    for i in range(point_index,0,-1):
        if num1[i-1]=='0':
            pass
        else:
            p=point_index-i
            sum=pow(2,p)+res
            res=sum

    #loop runs for the element after the loop
    for i in range(point_index+1,len(num1)):
        count=count-1
        if num1[i]=='0':
            pass
        else:
            sum=pow(2,count)+res
            res=sum
    print("the value of he binary number is ",res)

def main():
    num=float(input("enter the number ot covert binary"))
    point(num)

main()

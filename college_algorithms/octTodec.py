#write a program to convert octal number to decimal number

def oct(num):
    count=0
    res=0
    while(num>0):
        count=count+1
        last=num%10
        sum=8**(count-1)*last+res
        res=sum
        num=num//10
    print(res)
    # return res

def main():
    num=int(input("enter the octal number to covert decimal"))
    oct(num)
main()
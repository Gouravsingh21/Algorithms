# write a program to covert binary to decimal

def dec(num):
    count=0
    res=0
    while(num>0):
        count=count+1
        last=num%10
        if last==0:
            pass
        if last==1:
            sum=2**(count-1)+res
            res=sum
        num=num//10
    print("decimal number of given binary is:",res)
    return res

def main():
    num=int(input("enter the number ot covert binary"))
    dec(num)

main()

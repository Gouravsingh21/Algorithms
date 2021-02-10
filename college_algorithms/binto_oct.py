# Convert binary number to octal

def oct(num):
    res=''
    while(num>0):
        last_three=num%1000
        val=dec(last_three)
        sum=str(val)+res
        num=num//1000
        res=sum
    print(res)

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
    return res

def main():
    # num=101100
    num=int(input('enter the number '))
    oct(num)
main()

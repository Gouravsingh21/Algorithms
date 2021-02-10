def main():
    n=input("enter the number")
    c=int(input("1. binary to decimal \n2. octal to decimal \n3.hexdecimal to decimal"))
    decimal(n,c)
def decimal(n,c):
    if(c==1):
        a=n.split(".")
        new=int(a[0]+a[1])
        r=0
        p=-1*len(str(a[1]))
        while(new>0):
            b=new%10
            c=b*2**p
            r+=c
            new=new//10
        print(r)
    elif(c==2):
        a=n.split(".")
        new=int(a[0]+a[1])
        r=0
        p=-1*len(str(a[1]))
        while(new>0):
            b=new%10
            c=b*8**p
            r+=c
            new=new//10
            p+=1
        print(r)
    elif(c==3):
        a=n.split(".")
        print(a)
        b=a[0]+a[1]
        print(b)
        r=0
        p=-1*len(str(a[1]))
        for i in range((len(b)-1),-1,-1):
            if(b[i]>="0" and b[i]<="9"):
                c=int(b[i])
                d=c*16**p
                r+=d
                p+=1
            elif(b[i]>="A" and b[i]<="F"):
                t=ord(b[i])
                d=t*16**p
                r+=d
                p+=1
                
            else:
                print("wrong format")
                exit()
        print(r)
    else:
        print("wrong choice")
main()
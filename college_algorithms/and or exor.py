def And_or_exor():
    d=''
    a=input("enter the binary no.")
    b=input("enter the another binary no.")
    print("1.AND \n2.OR \n3.XOR")
    ch=int(input("enter the choice"))
    if(len(a)!=len(b)):
        if(len(a)>len(b)):
            r=len(a)-len(b)
            b=r*"0"+b
            print("changed no.",b)
        else:
            r=len(b)-len(a)
            a=r*"0"+a
            print("changed no.",a)
    c=len(a)
    if ch==1:
        for i in range(0,c):
            if (a[i]=='1' and b[i]=='1'):
                  d=d+'1'
            else:
                d=d+'0'
    elif(ch==2):
        for i in range(0,c):
            if(a[i]=='0' and b[i]=='0'):
                d=d+'0'
            else:
                d=d+'1'
    elif(ch==3):
        for i in range(0,c):
            if(a[i]=='1' and b[i]=='1'):
                d=d+'0'
            elif(a[i]=='0' and b[i]=='0'):
                d=d+'0'
            else:
                d=d+'1'
    else:
        print("invalid choice")

    return d     
def main():
    print(And_or_exor())
main()
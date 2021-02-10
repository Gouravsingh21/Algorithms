# Write a program to perform AND OR and XOR operation in two integers
def main():
    num1 = int(input('enter the First number'))
    num2 = int(input('enter the Second number'))
    print('1 for bitwise operator and 2 for logical operator')
    choice=int(input('enter the choice of operator'))
    if choice==1:
        print('1 for OR \n2 for AND \n3 for XOR')
        ch = int(input('enter the choice of operation'))
        bitwise(num1,num2,ch)
    elif choice==2:
        print('1 for OR \n2 for AND \n3 for XOR')
        ch = int(input('enter the choice of operation'))
        logical(num1,num2,ch)
    else:
        print("You entered the wrong choice")
    return 0

def bitwise(n1,n2,ch):
    if ch == 1:
        res = n1|n2
        print(res)
    elif ch==2:
        res=n1&n2
        print(res)
    elif ch==3:
        res=n1^n1
        print(res)
    else:
        print('wrong choice given')


def logical(n1,n2,ch):
    if ch == 1:
        res = n1 or n2
        print(res)
    elif ch==2:
        res=n1 and n2
        print(res)
    elif ch==3:
        res=n1 or n1
        print(res)
    else:
        print('wrong choice given')

main()
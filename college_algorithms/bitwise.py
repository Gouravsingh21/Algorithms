# write  a program to left shift or right shift of given number

def main():
    num=int(input('enter the first number'))
    sf=int(input('enter the second number'))
    print('Enter 1 for or \n 2 for and\n 3 for xor')
    ch=int(input('enter the choice'))
    shift(ch,num,sf)

def shift(ch,num,sf):
    if ch==1:
        num=num|sf
        print('or value of number  is',num)
    elif ch==2:
        num=num&sf
        print("and value of number is",num)
    elif ch==3:
        num=num^sf
        print("xor value of number is",num)
    else:
        print("wrong input")

main()

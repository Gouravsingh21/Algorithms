# write  a program to left shift or right shift of given number

def main():
    num=int(input('enter the number'))
    sf=int(input('how many places to shift'))
    print('Enter 1 for left shift \n 2 for right shift')
    ch=int(input('enter the choice'))
    shift(ch,num,sf)

def shift(ch,num,sf):
    if ch==1:
        num=num<<sf
        print('new number is',num)
    elif ch==2:
        num=num>>sf
        print(num)
    else:
        print('wrong choice')

main()

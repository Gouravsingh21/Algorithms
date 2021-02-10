# Menu driven program for number system conversion
def menu(ch):
    if ch==1:
        num1=float(input('enter the binary number to convert decimal'))
        num1 = str(num1)
        num1 = list(num1)
        res = 0
        count = 0
        point_index = num1.index('.')
        # loop runs for the elements before point
        for i in range(point_index, 0, -1):
            if str(num1[i-1])=='0':
                pass
            elif str(num1[i-1])=='1':
                p = point_index - i
                sum = pow(2, p) + res
                res = sum
            else:
                print('Wrong input given')
                exit()

        # loop runs for the element after the loop
        for i in range(point_index + 1, len(num1)):
            count = count - 1
            if num1[i] == '0':
                pass
            elif num1[i] == '1':
                sum = pow(2, count) + res
                res = sum
            else:
                print('Wrong input given')
                exit()

        print("the value of he binary number is ", res)
    elif ch==2:
        num = int(input("enter the octal number to covert decimal"))
        count = 0
        res = 0
        while (num > 0):
            count = count + 1
            last = num % 10
            if last>=0 and last<8:
                sum = 8 ** (count - 1) * last + res
                res = sum
                num = num // 10
            else:
                print('Wrong input given')
                exit()
        print(res)
        # return res
    elif ch==3:
        num=input('enter the hexadecimal number to covert decimal')
        item = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        num = list(num)
        if '.' in num:
            point_index = num.index('.')
        else:
            point_index = len(num)
        res = 0
        count = 0
        # loop runs for the elements before point
        for i in range(point_index - 1, -1, -1):
            if num[i] in item:
                p = point_index - i - 1
                sum = item.index(num[i]) * pow(16, p) + res
                res = sum
            else:
                print('Wrong input given')
                exit()
        # loop runs for the element after the loop
        for i in range(point_index + 1, len(num)):
            count = count - 1
            if num[i] in item:
                sum = item.index(num[i]) * pow(16, count) + res
                res = sum
            else:
                print('Wrong input given')
                exit()
        print(res)
    else:
        print('You entered the wrong choice')

def main():
    print('Menu driven program for conversion')
    print('Enter 1 for Binary to decimal \nEnter 2 for Octal to decimal\nEnter 3 for Hexa-decimal to decimal')
    ch=int(input('Enter Your choice'))
    menu(ch)

main()
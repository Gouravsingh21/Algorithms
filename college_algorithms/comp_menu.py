def main():
    print('1 for binary input or 2 for decimal input')
    choice=int(input('enter the choice of input'))
    if choice==1:
        num = input("enter the binary number")
        ch = int(input("enter the choice \n1 for one's compliment \n2 for two's compliemnt"))
        if ch == 1:
            print("1's complement of given number is ", one(num))
        elif ch == 2:
            print("2's complement of given number is", two(num))
        else:
            print('wrong choice given')
    elif choice==2:
        num=float(input("enter the decimal number"))
        num=convert_binary(num)
        num=float(num)
        num=int(num)
        num=str(num)
        ch = int(input("enter the choice \n1 for one's compliment \n2 for two's compliemnt"))
        if ch == 1:
            n=one(num)
            n=float(n)
            print(convert_decimal(n))
        elif ch == 2:
            n = two(num)
            n=float(n)
            print(convert_decimal(n))
        else:
            print('wrong choice given')
    else:
        print('wrong input')
        exit()


def convert_binary(n):
    split_num = str(n).split('.')
    int_part = int(split_num[0])
    decimal_part = '0.' + split_num[1]
    decimal_part = float(decimal_part)
    val1 = ''
    val2 = ''
    while (int_part != 0):
        rem = int_part % 2
        val1 = str(rem) + val1
        int_part = int_part // 2
    for i in range(1, 4):
        res = decimal_part * 2
        val2 = val2 + str(int(res))
        split_dec = str(res).split('.')
        decimal_part = '0.' + split_dec[1]
        decimal_part = float(decimal_part)
    res = val1 + '.' + val2
    return res

def convert_decimal(num1):
    num1 = str(num1)
    num1 = list(num1)
    res = 0
    count = 0
    point_index = num1.index('.')
    # loop runs for the elements before point
    for i in range(point_index, 0, -1):
        if str(num1[i - 1]) == '0':
            pass
        elif str(num1[i - 1]) == '1':
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
    return res

def one(num):
    result=''
    for index in range (0,len(num)):
        if num[index]=='0':
            result=result+'1'
        elif num[index]=='1':
            result=result+'0'
        else:
            print('Wrong input given')
            exit()
    return result

def two(num):
    check_num=one(num)
    comp2=num.rpartition('1')
    final_comp=one(comp2[0])
    res=final_comp+comp2[1]+comp2[2]
    return res

main()
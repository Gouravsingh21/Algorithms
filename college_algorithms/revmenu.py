# Convert Decimal to Binary,Octal and hexadecimal

def main():
    print("Enter 1 for binary\n2 for octal\n3 for hexadecimal")
    ch=int(input("Enter the choice you want"))
    n = float(input("Enter the decimal number"))
    menu(ch,n)

def menu(ch,n):
    if ch==1:
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
        for i in range(1,4):
            res = decimal_part * 2
            val2 = val2 + str(int(res))
            split_dec = str(res).split('.')
            decimal_part = '0.' + split_dec[1]
            decimal_part = float(decimal_part)
        print('binary value of the number is ',val1 + '.' + val2)

    elif ch==2:
        assert (n>8)
        split_num = str(n).split('.')
        int_part = int(split_num[0])
        decimal_part = '0.' + split_num[1]
        decimal_part = float(decimal_part)
        val1 = ''
        val2 = ''
        while (int_part != 0):
            rem = int_part % 8
            val1 = str(rem) + val1
            int_part = int_part // 8
        for i in range(1,4):
            res = decimal_part * 8
            val2 = val2 + str(int(res))
            split_dec = str(res).split('.')
            decimal_part = '0.' + split_dec[1]
            decimal_part = float(decimal_part)

        print('octal value of given decimal',val1+'.'+val2)
    elif ch==3:
        assert (n>16)
        split_num = str(n).split('.')
        int_part = int(split_num[0])
        decimal_part = '0.' + split_num[1]
        decimal_part = float(decimal_part)
        val1 = ''
        val2 = ''
        while (int_part != 0):
            rem = int_part % 16
            if rem>9:
                rem=chr(rem+55)
            val1 = str(rem) + val1
            int_part = int_part // 16
        for i in range(1, 4):
            res = decimal_part * 16
            if int(res)>9:
                val2=val2+chr(55+int(res))
            else:
                val2 = val2 + str(int(res))
            split_dec = str(res).split('.')
            decimal_part = '0.' + split_dec[1]
            decimal_part = float(decimal_part)
        print('hexadeimal value of the number is ', val1 + '.' + val2)

    else:
        print('wrong input')

main()
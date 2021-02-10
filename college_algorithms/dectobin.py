# Program to convert the decimal number to binary

def dectobin(n):
    split_num = str(n).split('.')
    int_part = int(split_num[0])
    decimal_part = '0.'+split_num[1]
    decimal_part=float(decimal_part)
    val1=''
    val2=''
    while(int_part!=0):
        rem=int_part%2
        val1=str(rem)+val1
        int_part=int_part//2
    while(decimal_part<=1):
        res=decimal_part*2
        val2=val2+str(int(res))
        decimal_part=res
    print(val1+'.'+val2)
def main():
    n=float(input("Enter the number to convert binary"))
    # n=43.167
    dectobin(n)

main()

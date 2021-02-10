# write a program to find sum of digit  of a number

def sum(num):
    sum=0
    while(num>0):
        digit=num%10
        sum=sum+digit
        num=num//10
    print('sum of digit is ',sum)
def main():
    sum(123)
    sum(237238)
    return 0
main()
# write a program to find factorial of a number

def fact(num):
    sum=1
    for i in range (1,num+1):
        res=i*(sum)
        sum=res
    print("factorial of number is",sum)
    return sum
def main():
    fact(5)
    fact(4)
    return 0
main()
# write a program to convert hexa decimal number to decimal number
def hex(num):
    item=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    num=list(num)
    if '.' in num:
        point_index=num.index('.')
    else:
        point_index=len(num)
    res=0
    count=0
    # loop runs for the elements before point
    for i in range(point_index-1, -1, -1):
        if num[i] in item:
            p = point_index - i-1
            sum = item.index(num[i])*pow(16, p) + res
            res = sum
        else:
            pass
    # loop runs for the element after the loop
    for i in range(point_index + 1, len(num)):
        count = count - 1
        if num[i] in item:
            sum = item.index(num[i])*pow(16,count) + res
            res = sum
        else:
            pass
    print(res)


def main():
    num=input("enter the octal number to covert decimal")
    hex(num)

main()


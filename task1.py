num=int(input("Enter a number"))
def fact(num):
    if num < 0:
        raise ValueError('Input must be a non-negtive integer')
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
print("the factorial number is : ",fact(num))
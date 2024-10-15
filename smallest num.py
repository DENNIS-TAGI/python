'''''
pyhton program to find the smallest number among 3 numbers
'''
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))
if num1<num2 and num1<num3:
    print("number 1 is the smallest number")
elif num2<num3 and num2<num1:
    print("number 2 is the smallest number")
else:
    print("number 3 is the smallest number")
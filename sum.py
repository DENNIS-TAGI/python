'''
python program to generate sum of  digits of a number
'''
number=int(input("enter a number:"))
sum=0
while(number>0):
      r=number%10
      number=number//10
      sum=sum+r
print("sum of digits:",sum)
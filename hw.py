#PYTHON CODE TO CHECK IS A NUMBER IS ARMSTRONG OR NOT

#Taking Input from user
num = int(input("Enter a number to check if its armstrong or not:"))

#Initializa sum
sum = 0

#Find sum of cube of each digit
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp //=10

#DISPLAY THE RESULT
if temp==sum:
    print(num,"is an armstrong number")
else:
     print(num,"is not an armstrong number")
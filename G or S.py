num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
    
if num1 % 2 == 0:
    print(num1, "is an even number")
else:
    print(num1, "is an odd number")

if num2 % 2 == 0:
    print(num2, "is an even number")
else:
    print(num2, "is an odd number")
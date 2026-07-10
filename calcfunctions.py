def add(X,Y):
    return X + Y
def subtract(X,Y):
    return X - Y
def multiply(X,Y):
    return X * Y
def divide(X,Y):
    return X / Y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
if choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
if choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
if choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
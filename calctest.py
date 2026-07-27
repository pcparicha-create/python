def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print("1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")

op= input("What operation would you like to do (1/2/3/4):")

n1= float(input("Your first number?:"))
n2= float(input("Your second number?:"))

if op=="1":
    print("The sum is ", add(n1,n2))
if op=="2":
    print("The difference is ", sub(n1,n2))
if op=="3":
    print("The product is ", mult(n1,n2))
if op=="4":
    try:
        print("The quotient is ", div(n1,n2))
    except ZeroDivisionError:
        print("Can't divide those! Can't divide by zero!")



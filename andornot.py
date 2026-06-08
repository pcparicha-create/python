a = 10
b = 12
c = 0

if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")


a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

    # Program to check the application of logical not operator

a = 10
b = 12
c = 12

# not is used here to reverse the result of (a == b)
print(not (a == b))

# not is used here to reverse the result of (b == c)
print(not (b == c))

a = "python"
b = "coding"

# not is used here to check that a is not equal to b
if not (a == b):
    print(a, 'and', b, 'are different.')

a = 4
b = 5

# not is used here to reverse the result of comparing both conditions
if not ((a == 1) == (b == 5)):
    print("Hello")

    height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height / 100) ** 2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
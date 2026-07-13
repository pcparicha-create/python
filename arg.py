def tc(bill,tip):
    total= bill*(1+ 0.01*tip)
    total = round(total, 2)
    print(f"TOTAL BILL IS: ${total}")

tc(120, 30)

#proj2

def cube(num):
    return num**3

def by3(num):
    if num%3==0:
        return cube(num)
    else:
        return False
    
print(by3(9))
print(by3(4))

#proj3

def factorial(num):
    '''this is a recursive function to find the factorial of a number'''

    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(176))
print(factorial(int(input("Enter a number to find the factorial: "))))

no = int(input("Enter a number: "))


total = 0

temp = no

while temp > 0:
    digit = temp % 10     
    total += digit ** 3   
    temp //= 10           


if total == no:
    print(no, "is an Armstrong number.")
else:
    print(no, "is not an Armstrong number.")
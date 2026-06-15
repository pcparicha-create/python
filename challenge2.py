N= int(input("Enter a numerator: "))
D= int(input("Enter a denominator: "))

if N%D == 0:
    print(N, "is divisible by", D)
else:
    print(N, "is not divisible by", D)
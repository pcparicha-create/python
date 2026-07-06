import random

guess = random.randint(1,50)

attempts= 5

print("❤️❤️❤️❤️❤️")

for i in range(5, 0, -1):
    pg = int(input("Guess a number from 1 through 50, wit 5 attempts:"))
    if pg ==guess:
        print("congratulations, your guess is correct.")
        break
    difference = abs(pg-guess)
    if difference <= 5:
        print("ice cold")
    if difference <= 10:
        print("cold")
    if difference <= 15:
        print("warm")
    if difference<= 20:
        print("hot")
    if attempts> 1:
        print("remaining heart", "❤️"*(attempts-1))
    else:
        print("no more left")
        print("secret number was", guess)



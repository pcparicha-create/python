import random  # importing module

playing = True  # initialise
number = str(random.randint(0, 9))  # random in-built function

print("\nI will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get it hero!")

# iterate loop till the condition is true
while playing:
    guess = input("Give me your best guess! \n")

    if number == guess:
        print("You win the game")
        print("The number was", number)
        break

    else:
        print("Your guess isn't quite right, try again. \n")



import random  # importing random module

while True:  # iterate loop
    user_action = input("Enter a choice (rock, paper, scissors): ")  # take input
    possible_actions = ["rock", "paper", "scissors"]

    # using random function
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    # display both outputs what is selected by you and computer

    # conditions to check who won the game
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    # take input for playing again
    play_again = input("Play again? (y/n): ")

    if play_again != "y":
        break




import math  # importing math module

# using ceil and floor function of math module
print("The floor and Ceiling value of 23.56 are: " +
      str(math.ceil(23.56)) + " " +
      str(math.floor(23.56)))

x = 10
y = -15

# using copysign function
print("The value of x after copying the sign from y is: " +
      str(math.copysign(x, y)))

# using fabs and gcd function
print("Absolute value of -96 and 56 are: " +
      str(math.fabs(-96)) + " " +
      str(math.fabs(56)))

print("The GCD of 2345 and 56755 is: " +
      str(math.gcd(2345, 56755)))
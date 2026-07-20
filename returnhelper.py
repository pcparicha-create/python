import random
rr=random.randint(5,100)
print("Hello! Welcome to the shop of Prad!")
q1= input("what do you want to buy today?")
print(f"{q1} costs {rr}")
q2= int(input(f"Can you please pay {rr}? (We accept cash and change is available!): "))

if q2 == rr:
    print("Thank you for buying our great goods!")
elif q2>rr:
    print(f"We wil give the change of amount: {q2-rr} ")
    print("Thank you for buying our great goods!")
elif q2<rr :
    print(f"you still are due to pay amount: {rr-q2} ")


    
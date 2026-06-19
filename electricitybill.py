# Electricity Bill Calculator using Nested Conditions

units = int(input("Enter the number of units consumed: "))

if units <= 50:
    cost_per_unit = 2.60
    tax = 25

else:
    if units < 100:
        cost_per_unit = 3.25
        tax = 35

    else:
        if units < 200:
            cost_per_unit = 5.26
            tax = 45

        else:
            cost_per_unit = 8.45
            tax = 75

bill_amount = units * cost_per_unit
total_bill = bill_amount + tax

print("The total electricity bill is: Rs.", total_bill)


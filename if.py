num= 3
if num > 0: 
    print(num, "is a positive number")

num= -5
if num < 0:
    print(num, "is a negative number")

actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!")
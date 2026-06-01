# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
SS = int(input("Social Studies: "))

# Let's calculate the percentage of marks
sum = math + english + science + SS
print("sum of math, english, science and Social Studies = ", sum)

perc = (sum / 400) * 100
print("Percentage = ", perc)
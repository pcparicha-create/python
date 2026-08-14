
grades = {
    "Pradyumna": 97.67,
    "Sneha": 92,
    "Jihan": 93,
    "Daniel": 91.6,
    "Jayden": 67
}
total = 0

for score in grades.values():
    total += score

average = total / len(grades)

print("Student Grade Book")
print("------------------")
print("Class average:", round(average, 2))


highest_score = max(grades.values())
lowest_score = min(grades.values())

top_student = max(grades, key=grades.get)
bottom_student = min(grades, key=grades.get)

print("Top scorer:", top_student, "-", highest_score)
print("Bottom scorer:", bottom_student, "-", lowest_score)


student = input("Enter a student's name to look up their grade: ")

grade = grades.get(student)

if grade is not None:
    print(student, "has a score of", grade, "%")
else:
    print("Sorry, that student is not in the grade book.")
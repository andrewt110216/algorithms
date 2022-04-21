# Hackerrank Problem
# Nested Lists
# Author: Andrew Tracey
# Completed: September 17, 2021

# --- PROBLEM DESCRIPTION ---
# Given the names and grades for each student in a class of  students,
#  store them in a nested list and print the name(s) of any student(s)
#  having the second lowest grade.

students = [['Harry', 37.21], ['Berry', 37.21],
            ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39],
            ['One More', 37.21]]

# Loop through all the students and find the lowest score
low = 100
for student in students:
    if student[1] < low:
        low = student[1]

# Remove all with the lowest score
for student in students:
    if student[1] == low:
        students.remove(student)

# Find the new lowest, now the second lowest
low = 100
for student in students:
    if student[1] < low:
        low = student[1]
print(students)

# Pull our all with lowest score
names = []
for student in students:
    print("Evaluating " + student[0])
    if student[1] == low:
        names.append(student[0])

names.sort()
for name in names:
    print(name)

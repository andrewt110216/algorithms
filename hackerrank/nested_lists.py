# Hackerrank Problem
# Nested Lists

# --- PROBLEM DESCRIPTION ---
# Given the names and grades for each student in a class of  students,
#  store them in a nested list and print the name(s) of any student(s)
#  having the second lowest grade.

students = [['Harry', 37.21], ['Berry', 37.21],
            ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# Create a new list with the students, sorted by score.
# Take each student, compare their score to each score in the sorted list,
#  and when you find a bigger score, insert to the sorted list there.
# If you make it to the end of list without finding greater score, at to end.

sorted_students = []
for student in students:
    for i in range(len(sorted_students) + 1):
        if i == len(sorted_students):
            sorted_students.append(student)
        else:
            if student[1] < sorted_students[i][1]:
                sorted_students.insert(i, student)
                break

print(f"Sorted List: {sorted_students}")

# Create a new list of any students with the second lost score
# Loop through the sorted list and find all with 2nd lowest score

students_second_lowest = []
second_lowest = 0
lowest_score = sorted_students[0][1]
still_looking = True  # True until we find the 2nd lowest score

for i in range(1, len(sorted_students)):
    if still_looking:
        if sorted_students[i][1] > lowest_score:
            second_lowest = sorted_students[i][1]
            students_second_lowest.append(sorted_students[i])
            still_looking = False
            continue
    if sorted_students[i][1] == second_lowest:
        students_second_lowest.append(sorted_students[i])

print(f"2nd Lowest Scorers: {students_second_lowest}")

# Loop through list of students with 2nd lowest scores, and alphabetize

students_second_lowest.sort()

print(f"Alphabetized 2nd Lowest Scorers: {students_second_lowest}\n")

for student in students_second_lowest:
    print(student[0])

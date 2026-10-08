##  Student Performance Analyzer

subjects = ["Bangla", "English", "Math", "Physics", "Chemistry"]

marks = []
credits = []
grade_points = []


for subject in subjects:

    mark = int(input(f"{subject}'s mark: "))

    # Validate marks
    while mark < 0 or mark > 100:
        print("Invalid mark!")
        mark = int(input(f"{subject}'s mark (0-100): "))

    credit = float(input(f"{subject}'s credit: "))

    marks.append(mark)
    credits.append(credit)


    if mark >= 80:
        grade = "A+"
        grade_point = 4.00

    elif mark >= 70:
        grade = "A"
        grade_point = 3.00

    elif mark >= 60:
        grade = "B"
        grade_point = 2.00

    elif mark >= 50:
        grade = "C"
        grade_point = 1.00

    else:
        grade = "F"
        grade_point = 0.00

    grade_points.append(grade_point)

    print(f"{subject}: {mark} → {grade} → {grade_point}")
    print()


total = sum(marks)
average = total / len(marks)

highest = max(marks)
lowest = min(marks)


highest_index = marks.index(highest)
lowest_index = marks.index(lowest)

highest_subject = subjects[highest_index]
lowest_subject = subjects[lowest_index]


total_point = 0
total_credit = 0

for i in range(len(subjects)):
    total_credit += credits[i]
    total_point += grade_points[i] * credits[i]

GPA = total_point / total_credit



if average >= 40:
    result = "PASS"
else:
    result = "FAIL"


print()
print("┌──────────────────────────────────┐")
print("│       STUDENT PERFORMANCE        │")
print("├──────────────────────────────────┤")
print(f"│ Total Mark      : {total:<12} │")
print(f"│ Average Mark    : {average:<12.2f} │")
print(f"│ Highest Mark    : {highest:<12} │")
print(f"│ Highest Subject : {highest_subject:<12} │")
print(f"│ Lowest Mark     : {lowest:<12} │")
print(f"│ Lowest Subject  : {lowest_subject:<12} │")
print(f"│ Result          : {result:<12} │")
print(f"│ Total Credits   : {total_credit:<12.2f} │")
print(f"│ Total Points    : {total_point:<12.2f} │")
print(f"│ GPA             : {GPA:<12.2f} │")
print("└──────────────────────────────────┘")

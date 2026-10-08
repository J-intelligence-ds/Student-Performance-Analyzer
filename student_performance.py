##  Student Performance Analyzer

subjects = ["Bangla", "English", "Math", "Physics", "Chemistry"]
marks = []
credits = []
grade_points = []

for subject in subjects:
    mark = int(input(f"{subject}'s mark:"))

    while mark > 100 or mark < 0:
        print("Invalid mark!!")
        mark = int(input(f"{subject}'s marks(0-100) :"))

    credit = float(input(f"{subject}'s credit:"))

    marks.append(mark)
    credits.append(credit)

    if mark >= 80:
       grade = "+A"
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

total_point = 0
total_credit = 0



total = sum(marks)
print("Total mark:", total)
average = total / len(marks)
print("Average mark:", average)
highest = max(marks)
print("Highest mark:", highest)
lowest = min(marks)
print("Lowest mark:", lowest)

highest_index = marks.index(highest)
lowest_index = marks.index(lowest)

highest_subject = subjects[highest_index]
print("Highest subject:", highest_subject)
lowest_subject = subjects[lowest_index]
print("Lowest subject:", lowest_subject)

if average >= 40:
    print("Result:Pass")
else:
    print("Result:Fail")


total_point = 0
total_credit = 0

for i in range(len(subjects)):
    total_credit += credits[i]
    total_point += grade_points[i] * credits[i]

GPA = total_point / total_credit


print("Total Grade Points:", total_point)
print("Total Credits:", total_credit)
print("GPA:", round(GPA, 2))

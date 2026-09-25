##  Student Performance Analyzer

subjects = ["Bangla","English","Math","Physics","Chemistry"]
marks = []
for subject in subjects:
    mark = int(input(subject + ":"))
    marks.append(mark)

total = sum(marks)
print("total marks:",total)
average = total / len(marks)
print("average marks:",average)
highest = max(marks)
print("highest mark:",highest)
lowest = min(marks)
print("lowest mark:",lowest)

highest_index = marks.index(highest)
lowest_index = marks.index(lowest)

highest_subject = subjects[highest_index]
print("highest subject:",highest_subject)
lowest_subject = subjects[lowest_index]
print("lowest subject:",lowest_subject)

if average >= 80:
    print("Grade:A+")
elif average >= 70:
    print("Grade:A")
elif average >= 60:
    print("Grade:B+")
elif average >= 50:
    print("Grade:B")
elif average >= 40:
    print("Grade:C+")
else:
    print("Fail")


if average >= 40:
    print("Result:Pass")
else:
    print("Result:Fail")

# 🎓 Student Performance Analyzer

A simple Python-based program that analyzes a student's academic performance using marks and credit hours. It calculates overall performance, assigns grades and grade points, and calculates the student's GPA.

## ✨ Features

- Takes marks for 5 subjects
- Validates marks between 0 and 100
- Takes credit hours for each subject
- Calculates total and average marks
- Finds the highest and lowest marks
- Identifies the highest- and lowest-scoring subjects
- Assigns grades and grade points
- Determines Pass/Fail status
- Calculates credit-weighted GPA
- Displays the final result in a formatted result box

## 📊 Grading System

| **Marks** | **Grade** | **Grade Point** |
| --------- | --------- | --------------- |
| 80–100    | A+        | 4.00            |
| 70–79     | A         | 3.00            |
| 60–69     | B         | 2.00            |
| 50–59     | C         | 1.00            |
| 0–49      | F         | 0.00            |

## 🧮 GPA Calculation

```text
GPA = Σ(Grade Point × Credit) / Σ(Credit)
```

## 💻 Example Output

```text
Bangla's mark: 85
Bangla's credit: 3
Bangla: 85 → A+ → 4.0

English's mark: 72
English's credit: 3
English: 72 → A → 3.0

Math's mark: 90
Math's credit: 3
Math: 90 → A+ → 4.0

Physics's mark: 65
Physics's credit: 3
Physics: 65 → B → 2.0

Chemistry's mark: 78
Chemistry's credit: 3
Chemistry: 78 → A → 3.0


┌──────────────────────────────────┐
│       STUDENT PERFORMANCE        │
├──────────────────────────────────┤
│ Total Mark      : 390            │
│ Average Mark    : 78.00          │
│ Highest Mark    : 90             │
│ Highest Subject : Math           │
│ Lowest Mark     : 65             │
│ Lowest Subject  : Physics        │
│ Result          : PASS           │
│ Total Credits   : 15.00          │
│ Total Points    : 45.00          │
│ GPA             : 3.00           │
└──────────────────────────────────┘
```

## 🛠️ Technologies Used

- Python

## 🧠 Concepts Practiced

This project helped me practice the following Python concepts:

- Variables and data types
- Lists
- `for` and `while` loops
- `if-elif-else` statements
- User input
- Input validation
- List indexing
- Built-in functions such as `sum()`, `max()`, `min()`, and `len()`
- Basic GPA calculation
- Formatted output

## 🎯 Project Purpose

The purpose of this project is to strengthen Python programming fundamentals by building a practical student performance analysis system.

## 🚀 Future Improvements

- Add support for multiple students
- Save student results to a file
- Add multi-semester CGPA calculation
- Add a graphical user interface (GUI)

## 👩‍💻 Author

**Jannat**  
Artificial Intelligence & Data Science Student
Artificial Intelligence & Data Science Student

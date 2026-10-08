# Student Performance Analyzer

A simple Python-based Student Performance Analyzer that calculates
students' academic performance from marks and credit hours.

## Features

- Takes marks for multiple subjects
- Validates marks between 0 and 100
- Takes credit hours for each subject
- Calculates total marks
- Calculates average marks
- Finds the highest mark
- Finds the lowest mark
- Identifies the highest-scoring subject
- Identifies the lowest-scoring subject
- Determines Pass/Fail based on average marks
- Assigns grades and grade points
- Calculates GPA using credit-weighted grade points

## Subjects

The program currently uses five subjects:

- Bangla
- English
- Math
- Physics
- Chemistry

## Grading System

| Marks | Grade | Grade Point |
|------:|:-----:|------------:|
| 80–100 | A+ | 4.00 |
| 70–79 | A | 3.00 |
| 60–69 | B | 2.00 |
| 50–59 | C | 1.00 |
| Below 50 | F | 0.00 |

> Note: The grading scale is based on the grading system used in this project and may differ from a university's official grading policy.

## How It Works

1. The program asks the user to enter marks for each subject.
2. It checks whether the marks are between 0 and 100.
3. The program asks for the credit of each subject.
4. It calculates the grade and grade point.
5. It calculates total and average marks.
6. It identifies the highest and lowest marks and their subjects.
7. It determines whether the student passed or failed.
8. Finally, it calculates the GPA based on subject credits.

## GPA Calculation

The GPA is calculated using:

GPA = Σ(Grade Point × Credit) / Σ(Credit)

## Technologies Used

- Python

## Python Concepts Used

This project helped practice:

- Variables
- Lists
- `for` loops
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- User input
- Input validation
- `sum()`
- `max()`
- `min()`
- `len()`
- `list.index()`
- f-strings
- Basic GPA calculation

## Example Output

```text
Bangla's mark: 85
Bangla's credit: 3

Bangla: 85 → A+ → 4.0

English's mark: 75
English's credit: 3

English: 75 → A → 3.0

...

Total mark: 390
Average mark: 78.0
Highest mark: 90
Lowest mark: 65
Highest subject: Math
Lowest subject: Chemistry
Result: Pass
Total Grade Points: 42.0
Total Credits: 15.0
GPA: 3.5

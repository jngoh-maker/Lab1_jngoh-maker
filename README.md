# Grade Evaluator & Archiver

## Overview

This project is my solution for **Lab 1 – Grade Evaluator & Archiver**. It reads student grades from a CSV file, validates the data, calculates the final grade and GPA, determines whether the student has passed or failed, and identifies formative assignments that are eligible for resubmission.

The project also includes a shell script that organizes and archives the project files.

---

## Project Files

```text
grade-evaluator.py     # Python program for evaluating grades
grades.csv             # Sample input data
organizer.sh           # Shell script for archiving project files
README.md              # Project documentation
```

---

## Features

* Reads assessment data from a CSV file.
* Validates that all scores are between **0 and 100**.
* Checks that:

  * Formative assessments contribute **60%**.
  * Summative assessments contribute **40%**.
  * Total assessment weight equals **100%**.
* Calculates the final grade.
* Calculates GPA using:

```text
GPA = (Final Grade / 100) × 5
```

* Determines whether the student passes or fails.
* Identifies failed formative assessments eligible for resubmission.
* Recommends the highest-weight failed formative assignment(s), including ties.

---

## Requirements

* Python 3
* Bash-compatible terminal (for `organizer.sh`)

---

## Running the Python Program

1. Make sure `grades.csv` is in the same folder as `grade-evaluator.py`.
2. Open a terminal in the project folder.
3. Run:

```bash
python grade-evaluator.py
```

4. When prompted, enter:

```text
grades.csv
```

---

## Running the Shell Script

1. Open a Bash-compatible terminal.
2. Make the script executable:

```bash
chmod +x organizer.sh
```

3. Run the script:

```bash
./organizer.sh
```

4. After it finishes, check:

* the `archive` folder
* `organizer.log`

to confirm the archive was created successfully.

---

## Sample CSV Format

```csv
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20
```

---

## Sample Output

```text
--- Processing Grades ---

Final Total Grade: 60.00/100
Final GPA: 3.00
Final Status: PASSED

Eligible for Resubmission:
- Group Exercise
- Functions and Debugging Lab
```

---

## Author

**Juliana Ngoh**

African Leadership University (ALU)

Bachelor of Software Engineering (BSE)

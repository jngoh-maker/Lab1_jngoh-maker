#!/usr/bin/python3

import csv
import sys
import os


def load_csv_data():
    filename = input(
        "Enter the name of the CSV file to process (e.g., grades.csv): "
    )

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: CSV file is empty or cannot be read.")
                sys.exit(1)

            required_columns = {'assignment', 'group', 'score', 'weight'}
            missing_columns = required_columns - set(reader.fieldnames)

            if missing_columns:
                print(
                    f"Error: CSV is missing required columns: "
                    f"{', '.join(sorted(missing_columns))}"
                )
                print(
                    f"Expected columns: {', '.join(sorted(required_columns))}"
                )
                print(f"Found columns: {', '.join(reader.fieldnames)}")
                sys.exit(1)

            row_count = 0
            for row in reader:
                row_count += 1

                if all(value.strip() == '' for value in row.values()):
                    print(f"Warning: Skipping empty row {row_count}.")
                    continue

                if not row.get('assignment', '').strip():
                    print(
                        f"Error: Row {row_count} has empty 'assignment' field."
                    )
                    sys.exit(1)

                if not row.get('group', '').strip():
                    print(
                        f"Error: Row {row_count} has empty 'group' field."
                    )
                    sys.exit(1)

                if not row.get('score', '').strip():
                    print(
                        f"Error: Row {row_count} has empty 'score' field."
                    )
                    sys.exit(1)

                if not row.get('weight', '').strip():
                    print(
                        f"Error: Row {row_count} has empty 'weight' field."
                    )
                    sys.exit(1)
                try:
                    score = float(row['score'])
                except ValueError:
                    print(
                        f"Error: Row {row_count} has invalid score "
                        f"'{row['score']}'. Must be a valid number."
                    )
                    sys.exit(1)

                try:
                    weight = float(row['weight'])
                except ValueError:
                    print(
                        f"Error: Row {row_count} has invalid weight "
                        f"'{row['weight']}'. Must be a valid number."
                    )
                    sys.exit(1)

                # Validate group is either 'Formative' or 'Summative'
                group = row['group'].strip().lower()
                if group not in ('formative', 'summative'):
                    print(
                        f"Error: Row {row_count} has invalid group "
                        f"'{row['group']}'. Must be 'Formative' or "
                        f"'Summative'."
                    )
                    sys.exit(1)

                assignments.append({
                    'assignment': row['assignment'].strip(),
                    'group': row['group'].strip(),
                    'score': score,
                    'weight': weight
                })

        if not assignments:
            print(
                "Error: No valid assignment data found in CSV file. "
                "File is empty or contains only headers."
            )
            sys.exit(1)

        return assignments

    except csv.Error as e:
        print(f"CSV parsing error: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"File I/O error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    # TODO: a) Check if all scores are percentage based (0-100)
    for item in data:
        if not (0.0 <= item['score'] <= 100.0):
            print(
                f"Validation Error: Score for "
                f"'{item['assignment']}' is "
                f"{item['score']}. Must be 0-100."
            )
            return

    # TODO: b) Validate total weights
    # (Total=100, Summative=40, Formative=60)
    summative_weight = sum(
        item['weight']
        for item in data
        if item['group'].strip().lower() == 'summative'
    )

    formative_weight = sum(
        item['weight']
        for item in data
        if item['group'].strip().lower() == 'formative'
    )

    total_weight = summative_weight + formative_weight

    if (
        total_weight != 100.0
        or summative_weight != 40.0
        or formative_weight != 60.0
    ):
        print("Weight Error: Weights do not meet requirements.")
        print(
            f"Summative: {summative_weight}/40 | "
            f"Formative: {formative_weight}/60 | "
            f"Total: {total_weight}/100"
        )
        return

    # TODO: c) Calculate the Final Grade and GPA
    total_summative_score = sum(
        item['score'] * (item['weight'] / 100)
        for item in data
        if item['group'].strip().lower() == 'summative'
    )

    total_formative_score = sum(
        item['score'] * (item['weight'] / 100)
        for item in data
        if item['group'].strip().lower() == 'formative'
    )

    final_grade = (
        total_summative_score +
        total_formative_score
    )

    gpa = (final_grade / 100) * 5.0

    print(f"Final Total Grade: {final_grade:.2f}/100")
    print(f"Final GPA: {gpa:.2f}")

    # TODO: d) Determine Pass/Fail status
    # (>= 50% in BOTH categories)

    summative_passed = (
        total_summative_score >= 20.0
    )

    formative_passed = (
        total_formative_score >= 30.0
    )

    if summative_passed and formative_passed:
        print("Final Status: PASSED")
    else:
        print("Final Status: FAILED")

    # TODO: e) Check for failed formative assignments (< 50%)
    # and determine which one(s) have the highest weight
    # for resubmission.

    failed_formatives = [
        item
        for item in data
        if (
            item['group'].strip().lower() == 'formative'
            and item['score'] < 50.0
        )
    ]

    if failed_formatives:

        max_weight = 0

        for item in failed_formatives:
            if item['weight'] > max_weight:
                max_weight = item['weight']

        eligible_for_resubmission = [
            item['assignment']
            for item in failed_formatives
            if item['weight'] == max_weight
        ]

        # TODO: f) Print the final decision
        # (PASSED / FAILED) and resubmission options

        print("\nEligible for Resubmission:")

        for assignment in eligible_for_resubmission:
            print(f"- {assignment}")

    else:
        print("\nEligible for Resubmission: None")


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)

#!/bin/bash

# Check if the archive directory exists; create it if it does not
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Create timestamp
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# Check if grades.csv exists
if [ -f "grades.csv" ]; then
    NEW_FILENAME="grades_$TIMESTAMP.csv"

    # Move grades.csv to archive folder
    mv grades.csv "archive/$NEW_FILENAME"

    # Create a new empty grades.csv
    touch grades.csv

    # Add details to log file
    echo "[$TIMESTAMP] Archived original grades.csv as $NEW_FILENAME in archive directory." >> organizer.log

    echo "Success! File archived as $NEW_FILENAME and workspace reset."
else
    echo "Error: 'grades.csv' not found in the current directory."
    exit 1
fi
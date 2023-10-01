# Employee Shift Analysis Program

This program analyzes employee shift data from an input file and identifies employees who meet specific criteria.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Input File Format](#input-file-format)
- [Program Output](#program-output)


## Description

The Employee Shift Analysis Program is designed to perform the following tasks:

1. Takes an input file containing employee shift data.
2. Iterates over the records in the file.
3. Identifies employees who meet the following criteria:
    - (a) Have worked for 7 consecutive days.
    - (b) Have less than 10 hours of time between shifts but greater than 1 hour.
    - (c) Have worked for more than 14 hours in a single shift.

The program outputs the names and positions of employees who meet these criteria.

## Requirements

- Python 3.x
- Required Python libraries (openpyxl, datetime)

## Usage

1. Clone this repository to your local machine.


Certainly! Below is a sample README.md file that you can use for your Git repository to document the task submission:

markdown
Copy code
# Employee Shift Analysis Program

This program analyzes employee shift data from an input file and identifies employees who meet specific criteria.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Input File Format](#input-file-format)
- [Program Output](#program-output)


## Description

The Employee Shift Analysis Program is designed to perform the following tasks:

1. Takes an input file containing employee shift data.
2. Iterates over the records in the file.
3. Identifies employees who meet the following criteria:
    - (a) Have worked for 7 consecutive days.
    - (b) Have less than 10 hours of time between shifts but greater than 1 hour.
    - (c) Have worked for more than 14 hours in a single shift.

The program outputs the names and positions of employees who meet these criteria.

## Requirements

- Python 3.x
- Required Python libraries (openpyxl, datetime)

## Usage

1. Clone this repository to your local machine:

Place the input file (your_file.xlsx) in the same directory as the program.

Run the program:
python analyze_shifts.py

The program will process the data and print the names and positions of employees who meet the specified criteria.
## Input File Format
The program expects the input file to be in Excel format (XLSX) and assumes the following columns:

Column 1: Employee Name
Column 2: Employee Position
Column 3: Start Time (in the format MM-DD-YYYY HH:MM:SS)
Column 4: End Time (in the format MM-DD-YYYY HH:MM:SS)
Please ensure that the input file follows this format.

## Program Output
The program will output the names and positions of employees who meet the specified criteria, along with the details of the criteria they meet.

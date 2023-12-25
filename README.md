# Employee Shift Analysis Program

## Overview

This Python program is designed to analyze employee shift data and identify specific patterns or issues related to their work schedules. The program takes input data containing employee shifts and generates insights such as consecutive working days, short breaks between shifts, and extended working hours.

## Features

- **Consecutive Working Days:** Identifies employees who have worked for a specified number of consecutive days.

- **Short Breaks Between Shifts:** Identifies employees who have less than a specified number of hours between consecutive shifts.

- **Extended Working Hours:** Identifies employees who have worked for more than a specified number of hours in a single shift.

## Getting Started



1. **Run the Program:**
    ```
    python bluejay.py input_data.csv
    ```
    Replace `input_data.csv` with the actual file path containing your employee shift data.

## Input Data Format

The program expects the input data to be in CSV format with the following columns:

- **Employee ID:** Unique identifier for each employee.
- **Shift Start Time:** Start time of the shift.
- **Shift End Time:** End time of the shift.

Example:

```
Employee ID,Shift Start Time,Shift End Time
WFS000153,2023-01-01 08:00:00,2023-01-01 16:00:00
WFS000523,2023-01-02 09:00:00,2023-01-02 17:00:00
...
```

## Sample Output

The program generates output similar to the following:

```
WFS000153, Active - Worked for 7 consecutive days
WFS000153, Active - Less than 10 hours between shifts
WFS000523, Active - Worked for 7 consecutive days
WFS000523, Active - Worked for 7 consecutive days
WFS000523, Active - Worked for more than 14 hours in a single shift
```

## Configuration

You can customize the program's behavior by modifying the configuration parameters in the `bluejay.py` file. Adjust the thresholds for consecutive working days, minimum break hours, and maximum shift hours based on your organization's policies.

## Acknowledgments

- Special thanks to the Python community for their invaluable contributions.

Feel free to contribute to and enhance this program to suit your organization's specific needs. If you encounter any issues or have suggestions for improvement, please create an issue or submit a pull request.

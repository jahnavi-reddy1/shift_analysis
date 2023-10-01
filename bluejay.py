import openpyxl
from datetime import datetime, timedelta

# Function to calculate the time difference between two datetime objects
def time_difference(start_time, end_time):
    return (end_time - start_time).total_seconds() / 3600  # Convert seconds to hours


workbook = openpyxl.load_workbook("C:\\Users\\jahnavi\\Downloads\\Assignment_Timecard.xlsx")
sheet = workbook.active


prev_employee = None
prev_end_time = None


for row in sheet.iter_rows(min_row=2, values_only=True):
    name = row[0]
    position = row[1]
    start_time_str = row[2]  
    end_time_str = row[3]    

   
    if start_time_str and end_time_str:
        
        try:
            
            start_time = start_time_str
            end_time = end_time_str
           
            if prev_employee == name:
                days_since_last_shift = (start_time - prev_end_time).days
                if days_since_last_shift <= 7:
                    print(f"{name}, {position} - Worked for 7 consecutive days")

            if prev_employee == name:
                hours_between_shifts = time_difference(prev_end_time, start_time)
                if 1 < hours_between_shifts < 10:
                    print(f"{name}, {position} - Less than 10 hours between shifts")

            
            hours_worked = time_difference(start_time, end_time)
            if hours_worked > 14:
                print(f"{name}, {position} - Worked for more than 14 hours in a single shift")

            
            prev_employee = name
            prev_end_time = end_time
            
        except Exception as e:
            print(str(e))
            print(f"Invalid date format for {name} - {start_time_str} or {end_time_str}")
            
workbook.close()

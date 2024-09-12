# Basic Input and Output

# Input Employee name
employee_name = input("Enter employee name: ")

# Inputting Work_day Hours
monday_hours = int(input("Enter hours worked on Monday: "))
tuesday_hours = int(input("Enter hours worked on Tuesday: "))
wednesday_hours = int(input("Enter hours worked on Wednesday: "))
thursday_hours = int(input("Enter hours worked on Thursday: "))
friday_hours = int(input("Enter hours worked on Friday: "))

# Calculating total hours in Week
total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours + friday_hours

# OutPut Total hours
print(f"Employee: {employee_name}, Total Hours Worked: {total_hours}")
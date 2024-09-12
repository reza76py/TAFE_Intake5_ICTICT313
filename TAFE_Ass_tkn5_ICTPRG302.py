
# Ask for the employee name
employee_name = input("Enter employee name: ")

# Initialize an empty list to store hours worked for each day
hours_worked = []

# Ask for hours worked each day
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    hours = int(input(f"Enter hours worked on {day}: "))
    hours_worked.append(hours)

# Calculate the total hours worked using the sum() function
total_hours = sum(hours_worked)

# Output the total hours worked
print(f"Employee: {employee_name}, Total Hours Worked: {total_hours}")

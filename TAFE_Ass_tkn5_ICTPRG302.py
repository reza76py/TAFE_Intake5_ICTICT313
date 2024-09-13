# Step 4: Handling Multiple Employees

# Initialize an empty list to store each employee's total hours
employee_records = []

# Loop to enter hours for 3 employees
for i in range(3):
    employee_name = input(f"Enter employee {i+1} name: ")
    hours_worked = []

    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        hours = int(input(f"Enter hours worked on {day}: "))
        hours_worked.append(hours)

        # Check for too few or too many hours worked
        if hours < 4:
            print(f"Insufficient hours worked on {day}")
        elif hours > 10:
            print(f"Too many hours worked on {day}")

    # Calculate the total hours
    total_hours = sum(hours_worked)
    employee_records.append((employee_name, total_hours))
    print(f"Employee: {employee_name}, Total Hours Worked: {total_hours}")

# Output the records for all employees
print("\nEmployee Records:")
for record in employee_records:
    print(f"Employee: {record[0]}, Total Hours: {record[1]}")

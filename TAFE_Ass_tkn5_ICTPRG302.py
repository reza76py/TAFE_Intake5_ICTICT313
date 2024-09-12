# Ask for the employee name
employee_name = input("Enter employee name: ")

# Initialize an empty list to store hours worked for each day
hours_worked = []

# Ask for hours worked each day and add conditional messages
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    hours = int(input(f"Enter hours worked on {day}: "))
    hours_worked.append(hours)

    # Check for too few or too many hours worked
    if hours < 4:
        print(f"Insufficient hours worked on {day}")
    elif hours > 10:
        print(f"Too many hours worked on {day}")

# Calculate the total hours worked using the sum() function
total_hours = sum(hours_worked)
if total_hours < 30:
    print("You didn’t do enough work this week")
elif total_hours > 40:
    print("You are working too hard!!")    


# Output the total hours worked
print(f"Employee: {employee_name}, Total Hours Worked: {total_hours}")

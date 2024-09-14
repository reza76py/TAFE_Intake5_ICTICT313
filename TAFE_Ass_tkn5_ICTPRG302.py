# Completed Code

import csv

# Function to save employee records to a CSV file
def save_to_file(filename="employee_hours.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Week", "Employee ID", "Employee Name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Total Hours"])
        for record in employee_records:
            writer.writerow(record)

# Function to enter hours for employees
def enter_hours():
    global employee_records  # Use the global employee_records list to track data

    week_number = int(input("Enter Current Working Week: "))
    
    for i in range(7):  # Loop for 7 employees
        employee_id = input(f"Enter Employee {i+1} ID: ")
        employee_name = input(f"Enter Employee {i+1} Name: ")
        hours_worked = []
        
        # Loop for 5 working days (Monday to Friday)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            hours = int(input(f"Enter hours worked on {day}: "))
            hours_worked.append(hours)
            
            # Check for too few or too many hours worked
            if hours < 4:
                print(f"Insufficient hours worked on {day}")
            elif hours > 10:
                print(f"Too many hours worked on {day}")
        
        # Calculate the total hours worked for the week
        total_hours = sum(hours_worked)
        
        # Append employee data to the employee_records list
        employee_records.append((week_number, employee_id, employee_name, *hours_worked, total_hours))
        
        # Display total hours for this employee
        print(f"Employee: {employee_name}, Total Hours Worked: {total_hours}")
        
        # Weekly work message
        if total_hours < 30:
            print(f"{employee_name} didn't do enough work this week.")
        elif total_hours > 40:
            print(f"{employee_name}, you are working too hard!!")
    
    # Save employee records to a file
    save_to_file()

# Function to generate weekly employee report
def generate_report():
    # Data structure to store weekly hours
    less_than_30 = 0
    more_than_40 = 0
    between_37_39 = 0

    # Process employee records
    for record in employee_records:
        total_hours = record[-1]  # Last element is the total weekly hours
        
        if total_hours < 30:
            less_than_30 += 1
        elif total_hours > 40:
            more_than_40 += 1
        elif 37 <= total_hours <= 39:
            between_37_39 += 1
    
    # Display the report
    print(f"\nWeekly Employee Report:")
    print(f"Number of employees who worked less than 30 hours: {less_than_30}")
    print(f"Number of employees who worked more than 40 hours: {more_than_40}")
    print(f"Number of employees who worked between 37-39 hours: {between_37_39}")

# Function to display employee records from the file (sorted by week number, latest first)
def display_records():
    try:
        with open("employee_hours.csv", mode='r') as file:
            reader = csv.reader(file)
            records = list(reader)
            records.pop(0)  # Remove header row

            # Sort records by week number in descending order
            sorted_records = sorted(records, key=lambda x: int(x[0]), reverse=True)

            num_records = int(input("Enter the number of most recent records you want to display: "))
            print("\nDisplaying records:")
            for record in sorted_records[:num_records]:
                print(record)
    except FileNotFoundError:
        print("No records found. Please enter employee hours first.")

# Main menu function
def main_menu():
    while True:
        print("\nWork From Home Tracker - Main Menu")
        print("1. Enter Daily Hours Worked")
        print("2. Produce Hours Worked Report")
        print("3. Display Employee Records")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            enter_hours()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            display_records()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# Global list to store employee records
employee_records = []

# Start the program
main_menu()

# Q9 - Employee Management System

employees = [
    ('SHRAVAN', '23BCA013', 'CMPICA'),
    ('MAHIR', '23BCA0250', 'CMPICA')
]

while True:
    print("""
Employee Management System
1. Display Employees
2. Add Employee
3. Remove Employee
4. Change Employee Name
5. Search Employee
6. Exit
""")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # Display Employees
        if not employees:
            print("No employees found.")
        else:
            print("\nEmployee List:")
            for emp in employees:
                print(f"Name: {emp[0]}, ID: {emp[1]}, Department: {emp[2]}")

    elif choice == '2':
        # Add Employee
        name = input("Enter new employee's name: ")
        emp_id = input("Enter new employee's ID: ")
        dept = input("Enter new employee's department: ")

        # Check for duplicate ID
        duplicate = False
        for emp in employees:
            if emp[1] == emp_id:
                duplicate = True
                break

        if duplicate:
            print("Employee with this ID already exists.")
        else:
            employees.append((name, emp_id, dept))
            print("Employee added successfully!")

    elif choice == '3':
        # Remove Employee
        emp_id = input("Enter the employee ID to remove: ")
        found = False
        for emp in employees:
            if emp[1] == emp_id:
                employees.remove(emp)
                found = True
                print("Employee removed successfully.")
                break
        if not found:
            print("Employee with this ID not found.")

    elif choice == '4':
        # Change Employee Name
        emp_id = input("Enter the employee ID to update name: ")
        found = False
        for i in range(len(employees)):
            if employees[i][1] == emp_id:
                new_name = input("Enter new name: ")
                employees[i] = (new_name, employees[i][1], employees[i][2])
                found = True
                print("Name updated successfully.")
                break
        if not found:
            print("Employee with this ID not found.")

    elif choice == '5':
        # Search Employee
        emp_id = input("Enter the employee ID to search: ")
        found = False
        for emp in employees:
            if emp[1] == emp_id:
                print(f"Employee found: Name: {emp[0]}, ID: {emp[1]}, Department: {emp[2]}")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == '6':
        # Exit
        print("Exiting Employee Management System.")
        break

    else:
        print("Please enter a valid choice (1 to 6).")

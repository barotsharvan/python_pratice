# Q11

student_ids = ('25BCA011', '25BCA012', '25BCA013')  

# Empty list to store student details
students = []

# Loop through each student id to get respective details
for i in range(len(student_ids)):
    print(f"Enter details for student ID: {student_ids[i]}")

    name = input("Enter student's name: ")     
    age = input("Enter student's age: ")          
    city = input("Enter student's city: ")      

    students.append([name, int(age), city])

print("\nStudent Details:")

# Display student information along with their IDs
for i in range(len(student_ids)):
    print(f"ID: {student_ids[i]}, Name: {students[i][0]}, Age: {students[i][1]}, City: {students[i][2]}")

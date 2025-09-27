#Dictionary
#Q17

students = {}

n = int(input("How many students? "))

for _ in range(n):
    name = input("Enter student's name: ")
    grade = input("Enter student's grade: ")
    students[name] = grade

search_name = input("Enter the name to search grade for: ")

if search_name in students:
    print(f"{search_name}'s grade is {students[search_name]}")
else:
    print(f"No grade found for {search_name}")

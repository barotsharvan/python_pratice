from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year
age = current_year - birth_year

print(f"\n{name}, your age is {age} years.")

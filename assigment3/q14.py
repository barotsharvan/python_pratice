#Q14

print("Enter all roll numbers separated by spaces:")
all_rolls = set(input().split())

print("Enter roll numbers of present students separated by spaces:")
present = set(input().split())

absent = all_rolls - present

print("\nAbsent students' roll numbers:")
for roll in absent:
    print(roll)

#Q13

print("Enter subjects chosen by first student separated by spaces:")
s1 = input().split()

print("Enter subjects chosen by second student separated by spaces:")
s2 = input().split()

set1 = set(s1)
set2 = set(s2)

common = set1 & set2
only_first = set1 - set2
all_subjects = set1 | set2

print("\nCommon subjects:")
for subj in common:
    print(subj)

print("\nSubjects only chosen by the first student:")
for subj in only_first:
    print(subj)

print("\nAll subjects chosen by both students:")
for subj in all_subjects:
    print(subj)

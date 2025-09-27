#Q15
name = input("Enter your full name: ")
name = name.replace(" ", "")
unique_chars = set(name)

print("Unique characters used:")
for ch in unique_chars:
    print(ch)

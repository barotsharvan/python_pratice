# Q8

week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

while True:
    choice = int(input("Enter your choice (0-6): "))
    if 0 <= choice <= 6:
        print("Day is:", week[choice])
        break
    else:
        print("Invalid Index")

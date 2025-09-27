# Q6 - Bank Account System

details = [
    [1001, 'Shravan', 5000],
    [1002, 'KUSH', 5000],
    [1003, 'Mahir', 5000]
]

acno = int(input("Enter Bank Account Number: "))

# Search for account
account = None
for record in details:
    if record[0] == acno:
        account = record
        break

if account:
    print(f"\nFound Details!\nAccount Number: {account[0]}\tAccount Holder: {account[1]}")

    while True:
        print("\nPress 1 || Check Balance")
        print("Press 2 || Deposit Balance")
        print("Press 3 || Withdraw Balance")
        print("Press 0 || Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            print("Your Balance:", account[2])

        elif choice == 2:
            amount = float(input("Enter Your Deposit Amount: "))
            account[2] += amount
            print("New Balance After Deposit:", account[2])

        elif choice == 3:
            if account[2] < 1000:
                print("Minimum Balance Required 1000!")
            else:
                amount = float(input("Enter Withdraw Amount: "))
                if account[2] - amount < 1000:
                    print("Insufficient Balance! You must keep at least 1000.")
                else:
                    account[2] -= amount
                    print("New Balance After Withdraw:", account[2])

        elif choice == 0:
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid Choice, Please Try Again...")

else:
    print("No Account Number and Holder Found. Sorry...")

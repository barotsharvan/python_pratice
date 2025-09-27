# Q4 - Task Manager

pending_tasks = ()
completed_tasks = ()

while True:
    print("\nTask Manager")
    print("1. Add task")
    print("2. Mark task done")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Write your new task: ")
        pending_tasks = pending_tasks + (task,)
        print("Task added!")

    elif choice == '2':
        if len(pending_tasks) == 0:
            print("No pending tasks! Please add some first.")
        else:
            print("Pending Tasks:")
            for i in range(len(pending_tasks)):
                print(i + 1, pending_tasks[i])

            num = input("Enter the number of the task you finished: ")

            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(pending_tasks):
                    done_task = pending_tasks[num - 1]
                    # Remove from pending and add to completed
                    pending_tasks = pending_tasks[:num - 1] + pending_tasks[num:]
                    completed_tasks = completed_tasks + (done_task,)
                    print("Task marked done:", done_task)
                else:
                    print("That's not a valid task number!")
            else:
                print("Please enter a valid number.")

    elif choice == '3':
        print("\nPending:")
        if len(pending_tasks) == 0:
            print("  No pending tasks.")
        else:
            for t in pending_tasks:
                print(" -", t)

        print("Completed:")
        if len(completed_tasks) == 0:
            print("  No completed tasks.")
        else:
            for t in completed_tasks:
                print(" -", t)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Please enter a choice from 1 to 4.")

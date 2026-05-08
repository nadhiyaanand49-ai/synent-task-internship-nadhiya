


tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == '1':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    
    elif choice == '2':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    
    elif choice == '4':
        print("Exiting To-Do List Program...")
        break

    else:
        print("Invalid choice. Please try again.")
def task_management_app():
    tasks = []  # Initialize an empty task list
    print("____WELCOME TO THE TASK MANAGEMENT APP____")

    # Add initial tasks
    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"\nToday's tasks are:\n{tasks}")

    # Operations Loop
    while True:
        print("\nOperations:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit")
        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if operation == 1:  # Add a new task
            add = input("Enter the task name you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:  # Update an existing task
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter the new task name = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}'.")
            else:
                print(f"Task '{updated_val}' not found in the list.")

        elif operation == 3:  # Delete a task
            delete_val = input("Enter the task name you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been successfully deleted.")
            else:
                print(f"Task '{delete_val}' not found in the list.")

        elif operation == 4:  # View all tasks
            print(f"Current tasks:\n{tasks}")

        elif operation == 5:  # Exit the program
            print("Exiting the Task Management App. Goodbye!")
            break

        else:  # Invalid choice
            print("Invalid choice! Please select a valid option.")

# Call the function to start the app
task_management_app()




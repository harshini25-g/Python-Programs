tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def mark_task_complete():
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if task_index >= 0 and task_index < len(tasks):
            del tasks[task_index]
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def menu():
    print("Welcome to the To-Do List Manager!")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Tasks")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()

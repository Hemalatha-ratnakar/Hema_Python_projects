# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task_description = input("Enter the task: ")
    tasks.append(task_description)
    print("Task added!")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
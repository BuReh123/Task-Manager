from taskManager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Clear All Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            print(manager.add_task(name, description, due_date))

        elif choice == "2":
            print("\nTasks:")
            print(manager.view_tasks())

        elif choice == "3":
            task_name = input("Enter task name to delete: ")
            print(manager.delete_task(task_name))

        elif choice == "4":
            print(manager.clear_tasks())

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

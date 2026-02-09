#David (Elvis) Etim

def todo_list ():
    tasks = []


    while True:
        print("Welcome to Elvis' TODO list")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose a number to proceed: ")

        if choice == "1":
            if tasks:
                print("Tasks: ")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

            else:
                print("No tasks found.")
        
        elif choice == "2":
            add_task = input("Enter a new task: ")
            tasks.append(add_task)
            print(f"{add_task} has been successfully added to the TODO list. ")

        elif choice == "3":
            edit_task_number = int(input("Enter task number you want to edit: "))
            if 0 < edit_task_number <= len(tasks):
                edited_task = input("Write the new task: ")
                tasks[edit_task_number - 1] = edited_task
                print(f"{edited_task} has been successfully updated to tasks. ")
            
            else:
                print("Invalid task number inputted.")

        elif choice == "4":
            task_number = int(input("Enter task number you want to remove: "))
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"{removed_task} has been successfully removed. ")

            else:
                print("Invalid task number inputted.")

        elif choice == "5":
            print("Goodbye! See ypou again soon.")   
            break

        else:
            print("Invalid option selected.")

todo_list()
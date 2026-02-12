#David (Elvis) Etim

class TaskManager:
    def __init__(self):
        self.tasks = []


    def view_task(self):
        if self.tasks:
            print("Tasks: ")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

        else:
                print("No tasks found.")

    def add_task(self):
        new_task = input("Enter a new task: ")
        self.tasks.append(new_task)
        print(f"{new_task} has been successfully added to the TODO list. ")

    def edit_task(self):
        edit_task_number = int(input("Enter task number you want to edit: "))
        if 0 < edit_task_number <= len(self.tasks):
            edited_task = input("Write the new task: ")
            self.tasks[edit_task_number - 1] = edited_task
            print(f"{edited_task} has been successfully updated to tasks. ")

        else:
                print("Invalid task number inputed.")

    def delete_task(self):
        task_number = int(input("Enter task number you want to remove: "))
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"{removed_task} has been successfully deleted. ")

        else:
            print("Invalid task number inputed. ")

    def exit_task(self):
        print("Goodbye! See you again soon. ")

    def main_menu(self):
        while True:

            print("Welcome to Elvis' TODO list")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Edit Task")
            print("4. Remove Task")
            print("5. Exit")
            choice = input("Choose a number to proceed: ")
         
                
            if choice == "1":
                self.view_task()
        
            elif choice == "2":
                self.add_task()

            elif choice == "3":
                self.edit_task()
             
            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                self.exit_task()   
                break

            else:
                print("Invalid option selected.")

 




task_manager = TaskManager()

task_manager.main_menu()

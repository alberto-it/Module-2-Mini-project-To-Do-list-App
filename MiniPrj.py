def get_user_choice():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice in menu_options.keys():
                return choice
            else:
                last_opt = list(menu_options.keys())[-1]
                print(f"Invalid choice. Please enter a number between 1 and {last_opt}.")
        except ValueError:
                print("Invalid input. Please enter a number.")

def add_task(task):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")       
    else:
        print("There are no tasks in the list.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    while True:
        try:
            task_nbr = int(input("Enter the number of the task to mark complete: "))
            if 1 <= task_nbr <= len(tasks):
                if tasks[task_nbr-1][:11] != "[COMPLETED]":
                    tasks[task_nbr-1] = f"[COMPLETED] {tasks[task_nbr-1]}"
                    print("Task marked complete.")
                return
            else:
                print("Invalid task number. Please enter a number between 1 and", len(tasks))
        except ValueError:
            print("Invalid input. Please enter a number.")

def delete_task(tasks):
    while True:
        if tasks:
            view_tasks(tasks)
        else:
            print("There are no tasks to delete.")
            return
        try:
            task_nbr = int(input("Enter the number of the task to delete: "))
            if 1 <= task_nbr <= len(tasks):
                del tasks[task_nbr-1]
                print("Task deleted.")
                return
            else:
                print("Invalid task number. Please enter a number between 1 and", len(tasks))
        except ValueError:
            print("Invalid input. Please enter a number.")

def bye(tasks):
    print("\nThanks for using the To-Do App!\n")
    exit()

menu_options = {
    1: add_task,
    2: view_tasks,
    3: mark_task_complete,
    4: delete_task,
    5: bye
}

print("\nWelcome to the To-Do List App!")
tasks = []
while True:
    menu_options[get_user_choice()](tasks)
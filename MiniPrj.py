def get_user_choice():
    print("\nMenu:")
    if tasks:
        print("1. Add another task")
        print("2. View tasks")
        print("3. Mark a task as complete ✅" if len(tasks) != sum(1 for task in tasks if task[0] == "✅") else "3. Mark a task as complete (currently all are ✅)")
        print("4. Delete a task" if tasks else "4. Delete a task (currently none to delete)")
    else:
        print("1. Add first task")
        print("2. View tasks (currently nothing to view)")
        print("3. Mark a task as complete (currently nothing to ✅)")
        print("4. Delete a task (currently nothing to delete)")
    print("5. Quit")
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice in range(1,6):
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
                print("Invalid input. Please enter a number.")

def add_task(task):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully.")
    view_tasks(tasks)

def view_tasks(tasks):
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")       
    else:
        print("There are no tasks in the list.")

def mark_task_complete(tasks):
    while True:
        if tasks:
            view_tasks(tasks)
        else:
            print("There are no tasks to mark as complete.")
            break
        try:
            task_nbr = int(input("Enter the number of the task to mark complete: "))
            if 1 <= task_nbr <= len(tasks):
                if tasks[task_nbr-1][0] == "✅":
                    print(f"Task #{task_nbr} was already marked as completed ✅")
                else:
                    tasks[task_nbr-1] = f"✅ {tasks[task_nbr-1]}"
                    print(f"Task #{task_nbr} marked complete ✅")
                    view_tasks(tasks)
                break
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
            break
        try:
            task_nbr = int(input("Enter the number of the task to delete: "))
            if 1 <= task_nbr <= len(tasks):
                del tasks[task_nbr-1]
                print(f"Task # {task_nbr} deleted.")
                view_tasks(tasks)
                break
            else:
                print("Invalid task number. Please enter a number between 1 and", len(tasks))
        except ValueError:
            print("Invalid input. Please enter a number.")

menu_options = {
    1: add_task,
    2: view_tasks,
    3: mark_task_complete,
    4: delete_task
}

print("\nWelcome to the To-Do List App!")
tasks = []
while True:
    choice = get_user_choice()
    if choice == 5:  
        print("\nThanks for using the To-Do App!\n")
        break 
    else:
        menu_options[choice](tasks)

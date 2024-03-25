The main function of the program is get_user_choice(), which shows users their options and has them choose which one they may select
(the program continually loops through get_user_choice() until the Quit option is selected). The choices are validated.
A dictionary called menu_options contains five functions corresponding to the five Menu choices.
Once users selects their option in get_user_choice(), the corresponding dictionary option is executed:
  add_task() - Appends inputed task to tasks list.
  view_tasks() - Prints the tasks list or "no tasks in list" if empty.
  mark_task_complete() - Adds [COMPLETED] to the front of the selected task (with validation). Does nothing if task was already marked.
  delete_task() - If tasks list is not empty, shows tasks and asks users to enter which one to delete (with validations).
  bye() - Thanks the user and exits program.

def display():
    print("\nCommand Menu:")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Mark Item as Completed")
    print("4. Delete Item from To-Do List")
    print("5. Exit")
def view_list(todo_list):
    print("\nTo-Do List:")
    if not todo_list:
        print("No tasks.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['task']} - {'DONE' if task['done'] else 'TODO'}")
def add_task(todo_list):
    task = input("\nEnter the task to add: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added to the To-Do List.")
def mark_complete(todo_list):
    view_list(todo_list)
    task_index = int(input("\nEnter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]['done'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")
def del_task(todo_list):
    view_list(todo_list)
    task_index = int(input("\nEnter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(todo_list):
        del todo_list[task_index]
        print("Task deleted from the To-Do List.")
    else:
        print("Invalid task index.")
def main():
 todo_list = []
 while True:
   display()
   choice = input("\nEnter your choice: ")
   if choice == '1':
     view_list(todo_list)
   elif choice == '2':
     add_task(todo_list)
   elif choice == '3':
     mark_complete(todo_list)
   elif choice == '4':
     del_task(todo_list)
   elif choice == '5':
     print("Exiting the program. Goodbye!")
     break
   else:
     print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
